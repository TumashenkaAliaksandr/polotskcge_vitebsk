# Generated by Django 5.0.3 on 2024-08-01 14:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0131_alter_ticks_name_map'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpidemialogyInf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл (для админ)', max_length=350)),
                ('name_typical', models.CharField(default='Тайтл', max_length=350)),
                ('description', models.TextField(default='Описание')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата Публикации')),
            ],
            options={
                'verbose_name': 'Эпидемиалогия (статьи)',
                'verbose_name_plural': 'Эпидемиалогия (статьи)',
            },
        ),
        migrations.CreateModel(
            name='EpidemialogyName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл для админки', max_length=350)),
                ('name_typical', models.CharField(default='Тайтл', max_length=350)),
            ],
            options={
                'verbose_name': 'Эпидемиалогия (Тайтл)',
                'verbose_name_plural': 'Эпидемиалогия (Тайтл)',
            },
        ),
        migrations.CreateModel(
            name='EpidemialogySingleName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл для админки', max_length=350)),
                ('name_typical', models.CharField(default='Тайтл', max_length=350)),
            ],
            options={
                'verbose_name': 'Эпидемиалогия статьи (Тайтл)',
                'verbose_name_plural': 'Эпидемиалогия статьи (Тайтл)',
            },
        ),
    ]