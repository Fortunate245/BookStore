# Generated by Django 3.1.4 on 2020-12-01 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_url',
            field=models.URLField(default='https://www.bookcamp.com'),
        ),
    ]