# Generated by Django 5.1.1 on 2024-10-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_book_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.FloatField(default=1.0, max_length=5),
        ),
    ]