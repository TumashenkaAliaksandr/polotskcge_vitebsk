# Generated by Django 5.0.3 on 2024-09-09 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0202_remove_cities_description_three_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citydescription',
            options={'verbose_name': 'Здоровые города и поселки - Описание города', 'verbose_name_plural': 'Здоровые города и поселки - Описания городов'},
        ),
    ]
