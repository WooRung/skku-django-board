from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect

from datetime import datetime

from django.urls import reverse

from .models import Board


# 1. is_active = True인 사람만 html에서 rendering
# 2. (심화) 모두 rendering하되, is_active가 True인 사람만 글자색 파란색 표시
# def index(request):
#     now = datetime.now()
#     now = now.strftime("%Y.%m.%d %H:%M:%S")
#     name_list = [{
#         'name': "신윤수", "is_active": True
#     }, {
#         "name": "장지혜", "is_active": False
#     }, {
#         "name": "전인오", "is_active": True
#     }]
#     return render(request,
#                   "board/index.back.html",
#                   {"name": "신윤수", "now": now, "name_list": name_list})

def index(request):
    board_list = Board.get_active_board()
    return render(request,
                  'board/index.html',
                  {"board_list": board_list})


def board_detail(request, board_id):
    try:
        board = Board.get_active_board().prefetch_related("comment_set").get(id=board_id)
        comment_form = CommentForm(initial={'board': board})
    except Board.DoesNotExist as e:
        raise Http404("게시글이 없습니다.")
    # 1. board/templates/board/detail.html 만들어라.
    # 2. 127.0.0.1:8000/board/<int:board_id> 에 요청을 보내면 id에 맞는 게시글의 제목,
    # 내용이 나오도록 하여라.
    return render(request, "board/detail.html",
                  {'board': board, 'comment_form': comment_form})


from django.shortcuts import redirect
from django.urls import reverse

from .forms import BoardForm, CommentForm


def board_create(request):
    form = BoardForm()
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("board:index"))

    return render(request,
                  "board/create.html",
                  {"form": form})


def board_edit(request, board_id):
    # board = get_object_or_404(Board, id=board_id)
    # if not board.is_active():
    #     raise Http404("게시물이 없습니다.")
    #### 위와 아래는 같습니다.
    board = get_object_or_404(Board.get_active_board(), id=board_id)

    form = BoardForm({'title': board.title, 'content': board.content})

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            board.title = data['title']
            board.content = data['content']
            board.save()
            return redirect(reverse('board:detail', kwargs={'board_id': board.id}))
    return render(request, 'board/edit.html', {'form': form, 'board': board})


def board_delete(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if not board.is_active():
        print(board.is_active())
        raise Http404("게시물이 없습니다.")

    board.delete()
    return redirect(reverse('board:index'))


def board_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            board = form.cleaned_data['board']

    return redirect(reverse('board:detail', kwargs=({'board_id': board.id})))
