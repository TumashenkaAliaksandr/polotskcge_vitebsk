# Generated by Django 5.0.3 on 2024-07-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0106_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='description_two',
            field=models.TextField(default='Описание 2'),
        ),
    ]