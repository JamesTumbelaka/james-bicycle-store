# Generated by Django 4.2.5 on 2023-09-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_product_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product", name="amount", field=models.PositiveIntegerField(),
        ),
    ]
