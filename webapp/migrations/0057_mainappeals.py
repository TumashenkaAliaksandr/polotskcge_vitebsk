# Generated by Django 5.0.3 on 2024-06-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0056_vacancies_alter_duties_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainAppeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=300)),
                ('name_two', models.CharField(default='Тайтл 2', max_length=300)),
                ('name_three', models.CharField(default='Тайтл 3', max_length=300)),
                ('appeals_desc', models.CharField(default='Описание под тайтл', max_length=300)),
                ('appeals_desc_two', models.CharField(default='Описание', max_length=7000)),
                ('appeals_desc_three', models.CharField(default='Описание 2', max_length=7000)),
                ('appeals_desc_four', models.CharField(default='Описание 3', max_length=7000)),
            ],
            options={
                'verbose_name': 'Обращения главная',
                'verbose_name_plural': 'Обращения главная',
            },
        ),
    ]
