from django.db import models

from django.core import validators
from django.utils import timezone


class Board(models.Model):
    id = models.AutoField(primary_key=True)  # integer(auto-increment)
    title = models.CharField("제목", max_length=255,
                             validators=[
                                 validators.MinLengthValidator(2, "최소 세 글자 이상이어야 합니다.")
                             ])  # varchar(255)
    content = models.TextField("내용", validators=[validators.MinLengthValidator(10, "최소 10글자")])  # Text
    created_at = models.DateTimeField(auto_now_add=True)  # datetime
    updated_at = models.DateTimeField(auto_now=True)  #
    deleted_at = models.DateTimeField(null=True)

    @classmethod
    def get_active_board(cls):
        return cls.objects.filter(deleted_at__isnull=True)

    @classmethod
    def active_list(cls):
        return cls.objects.filter(deleted_at__isnull=True)

    def delete(self):
        self.deleted_at = timezone.now()
        return self.save()

    def is_active(self):
        return not bool(self.deleted_at)

    def __str__(self):
        return f"{self.pk} - {self.title}"


class Comment(models.Model):
    board = models.ForeignKey("Board", null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=255)  # varchar(255)
    created_at = models.DateTimeField(auto_now_add=True)  # datetime
    updated_at = models.DateTimeField(auto_now=True)  #
