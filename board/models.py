from django.db import models


class Board(models.Model):
    id = models.AutoField(primary_key=True)  # integer(auto-increment)
    title = models.CharField(max_length=255)  # varchar(255)
    content = models.TextField()  # Text
    created_at = models.DateTimeField(auto_now_add=True)  # datetime
    updated_at = models.DateTimeField(auto_now=True)  #


class Comment(models.Model):
    board = models.ForeignKey("Board", null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=255)# varchar(255)
    created_at = models.DateTimeField(auto_now_add=True)  # datetime
    updated_at = models.DateTimeField(auto_now=True)  #