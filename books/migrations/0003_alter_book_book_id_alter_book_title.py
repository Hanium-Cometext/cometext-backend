# Generated by Django 4.2.5 on 2023-09-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_options_remove_book_writer_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(default='', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
