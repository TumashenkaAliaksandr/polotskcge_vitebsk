# Generated by Django 5.0.3 on 2024-06-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0042_remove_hotlinehours_phone_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotlinehours',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='hotlinehours',
            name='date_hotline',
            field=models.CharField(default='Дата Проведения прям линии', max_length=100),
        ),
    ]
