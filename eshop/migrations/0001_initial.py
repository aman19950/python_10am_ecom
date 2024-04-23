# Generated by Django 4.2.6 on 2024-04-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                (
                    "first_name",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "email",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                (
                    "password",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                ("mobile", models.BigIntegerField(default=0)),
                (
                    "gender",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
            ],
        ),
    ]
