from django.http import HttpResponse


def index(request):
    user_profile = {
        '이름': "신윤수",
        '별명': "ys"
    }
    result = "<h3>나의 프로필</h3> <ul>"
    for k, v in user_profile.items():
        result += f"<li>{k}: {v}</li>"
    result += "</ul>"
    return HttpResponse(result)
