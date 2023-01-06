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


# Create your views here.
def index(request):
    return render(request, 'user/profile.html')
