# Generated by Django 5.1 on 2024-08-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0005_author_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.TextField(default=' ', max_length=200),
        ),
    ]