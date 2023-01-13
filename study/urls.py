from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='students')

urlpatterns = [
   # path('students/', views.StudentView.as_view()),
   # path('students/<int:pk>', views.StudentDetailView.as_view()),
   # path('students/', views.StudentViewSet.as_view({
   #    "get": "list",
   #    "post": "create"
   # })),
   # path('students/<int:pk>/', views.StudentViewSet.as_view({
   #    "get": "retrieve",
   #    "put": "update",
   #    "delete": "destroy"
   # })),
   path('score/', views.ScoreView.as_view()),
] + router.urls