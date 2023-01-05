from django.db import models

from django.core import validators


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


    def delete(self):
        self.deleted_at = timezone.now()
        return self.save()

    def is_active(self):
        return not bool(self.deleted_at)

    @classmethod
    def active_list(cls):
        return cls.objects.filter(deleted_at__isnull=True)


class Comment(models.Model):
    board = models.ForeignKey("Board", null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=255)  # varchar(255)
    created_at = models.DateTimeField(auto_now_add=True)  # datetime
    updated_at = models.DateTimeField(auto_now=True)  #
