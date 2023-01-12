from django.urls import path
from . import api

urlpatterns = [
    path('', api.board_list, name='api_board_list'),
    path('<int:board_id>', api.board_api, name='api_board')
]
