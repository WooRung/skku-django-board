# Generated by Django 4.1.4 on 2023-01-05 04:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="board",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="board",
            name="content",
            field=models.TextField(
                validators=[django.core.validators.MinLengthValidator(10, "최소 10글자")],
                verbose_name="내용",
            ),
        ),
        migrations.AlterField(
            model_name="board",
            name="title",
            field=models.CharField(
                max_length=255,
                validators=[
                    django.core.validators.MinLengthValidator(2, "최소 세 글자 이상이어야 합니다.")
                ],
                verbose_name="제목",
            ),
        ),
    ]
