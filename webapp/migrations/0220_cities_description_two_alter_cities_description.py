# Generated by Django 5.0.3 on 2024-10-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0219_cities_file_desc_cities_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='description_two',
            field=models.TextField(default='Описание для страницы Поселка'),
        ),
        migrations.AlterField(
            model_name='cities',
            name='description',
            field=models.TextField(default='Описание для страницы Города/Посёлки'),
        ),
    ]
