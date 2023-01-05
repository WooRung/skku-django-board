from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    # /board/1
    path('', views.index, name="index"),
    path('<int:board_id>',
         views.board_detail,
         name="detail"),
    path('create', views.board_create, name="create"),

    path('comment', views.board_comment, name='comment'),
    path('<int:board_id>/edit', views.board_edit, name='edit'),
    path('<int:board_id>/delete', views.board_delete, name='delete')

]
