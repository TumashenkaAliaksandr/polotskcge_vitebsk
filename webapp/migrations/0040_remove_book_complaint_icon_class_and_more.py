# Generated by Django 5.0.3 on 2024-06-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0039_book_complaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_complaint',
            name='icon_class',
        ),
        migrations.AlterField(
            model_name='book_complaint',
            name='description',
            field=models.TextField(default='Book Description'),
        ),
        migrations.AlterField(
            model_name='book_complaint',
            name='name',
            field=models.CharField(default='Book Name', max_length=100),
        ),
    ]
