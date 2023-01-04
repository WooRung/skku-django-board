from django.urls import path
from . import views

urlpatterns = [
    # /board/1
    path('', views.index, name="index"),
    path('<int:board_id>',
         views.board_detail,
         name="detail"),
]
