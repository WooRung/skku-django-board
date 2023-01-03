from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime


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
#                   "board/index.html",
#                   {"name": "신윤수", "now": now, "name_list": name_list})

def index(request):
    return render(request, 'board/layout1.back.html')
