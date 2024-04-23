# Generated by Django 4.2.6 on 2024-04-15 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("eshop", "0002_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                    "product_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("product_image", models.ImageField(upload_to="upload/product/")),
                (
                    "product_description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("product_price", models.IntegerField()),
                (
                    "product_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="eshop.category"
                    ),
                ),
            ],
        ),
    ]
