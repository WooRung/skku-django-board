from django.forms import model_to_dict
from django.http import JsonResponse, Http404

from .models import Board
import json

"""
/board                  GET     게시물 리스트 조회
/board/<int:board_id>   GET     게시물 상세 조회
/board                  POST    게시물 등록
/board/<int:board_id>   PUT     게시물 수정
/board/<int:board_id>   DELETE  게시물 삭제
"""


# /board GET     게시물 리스트 조회
# /board POST    게시물 등록
def board_list(request):
    if request.method == 'GET':
        board_list = Board.objects.all()
        return JsonResponse(list(board_list.values()), safe=False)
    elif request.method == 'POST':
        print(request.body)
        # json.dumps = python obj -> json
        # json.loads = json -> python obj
        data = json.loads(request.body)
        print(data)
        # data에 board정보가 있다 -> DB에 insert까지 하시죠.
        # return은 board정보를 echoing
        board = Board(title=data['title'], content=data['content'])
        board.save()
        return JsonResponse(model_to_dict(board), safe=False)


# GET: /board/<int:boardId>
# PUT 구현
# DELETE구현
def board_api(request, board_id):
    if request.method not in ['GET', 'PUT', 'DELETE']:
        raise Http404("에러")
    board = Board.objects.get(id=board_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        board.title = data['title']
        board.content = data['content']
        board.save()
    elif request.method == 'DELETE':
        board.delete()

    return JsonResponse(model_to_dict(board))
