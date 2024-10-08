# Generated by Django 5.0.3 on 2024-06-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0049_organ_title_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Up_Organ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Фамилия Имя и Отчество', max_length=100)),
                ('post', models.CharField(default='Должность', max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('reception_time', models.CharField(default='Время Приема', max_length=100)),
            ],
            options={
                'verbose_name': 'Вышестоящий орган данные',
                'verbose_name_plural': 'Вышестоящий орган данные',
            },
        ),
    ]
