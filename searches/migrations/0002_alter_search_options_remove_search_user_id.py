# Generated by Django 4.2.5 on 2023-09-17 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={},
        ),
        migrations.RemoveField(
            model_name='search',
            name='user_id',
        ),
    ]