from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

def index(request):
    now = datetime.now()
    now = now.strftime("%Y.%m.%d %H:%M:%S")
    return render(request,
                  "board/index.html",
                  {"name": "신윤수", "now":now})

