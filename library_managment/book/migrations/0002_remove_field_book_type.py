# Generated by Django 4.1 on 2022-10-27 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='Book_Type',
        ),
    ]
