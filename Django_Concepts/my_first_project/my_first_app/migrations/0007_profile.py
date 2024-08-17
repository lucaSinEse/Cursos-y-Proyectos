# Generated by Django 5.1 on 2024-08-17 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0006_author_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField()),
                ('biography', models.TextField(max_length=500)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='my_first_app.author')),
            ],
        ),
    ]
