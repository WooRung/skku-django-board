from django.http import Http404
from django.shortcuts import render

from datetime import datetime
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
    board_list = Board.objects.all()
    return render(request,
                  'board/index.html',
                  {"board_list": board_list})


def board_detail(request, board_id):
    try:
        board = Board.objects.prefetch_related("comment_set").get(id=board_id)
    except Board.DoesNotExist as e:
        raise Http404("게시글이 없습니다.")
    # 1. board/templates/board/detail.html 만들어라.
    # 2. 127.0.0.1:8000/board/<int:board_id> 에 요청을 보내면 id에 맞는 게시글의 제목,
    # 내용이 나오도록 하여라.
    return render(request, "board/detail.html", {'board': board})
