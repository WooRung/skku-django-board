# Generated by Django 4.1.5 on 2023-01-13 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=30)),
            ],
        ),
    ]
