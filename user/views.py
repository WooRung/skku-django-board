# from django.http import HttpResponse
#
#
# def index(request):
#     user_profile = {
#         '이름': "신윤수",
#         '별명': "ys"
#     }
#     result = "<h3>나의 프로필</h3> <ul>"
#     for k, v in user_profile.items():
#         result += f"<li>{k}: {v}</li>"
#     result += "</ul>"
#     return HttpResponse(result)
from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    if not request.session.get('history'):
        request.session['history'] = []
    request.session['history'] = request.session['history'] + [datetime.now().strftime('%H:%M:%S')]
    print(request.session['history'])
    # print(request.session)
    # print("session 확인")
    # for k, v in request.session.items():
    #     print(k, v)
    # print(request.user)
    # print(request.user.is_authenticated)
    # print(request.user.is_superuser)
    # print(request.user.is_staff)
    # print(request.user.email)
    return render(request, 'user/profile.html')
