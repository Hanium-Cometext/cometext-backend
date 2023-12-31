# Generated by Django 4.2.5 on 2023-09-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searches', '0004_alter_search_search_id_alter_search_sentence'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entire', models.CharField(max_length=200)),
                ('philosophy', models.CharField(max_length=200)),
                ('Religion', models.CharField(max_length=200)),
                ('Science', models.CharField(max_length=200)),
                ('Art', models.CharField(max_length=200)),
                ('Language', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='search',
            name='search_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='sentence',
            field=models.TextField(default='', help_text='Search Sentence', null=True),
        ),
    ]
