# Generated by Django 5.0.3 on 2024-08-01 18:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0138_rename_photo_bg_epidemialogytipical_photo_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImmunoprophylaxisInf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=350)),
                ('description', models.TextField(default='Описание')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата Публикации')),
            ],
            options={
                'verbose_name': 'Иммунопрофилактика (название и краткое описание статьи)',
                'verbose_name_plural': 'Иммунопрофилактика (название и краткое описание статьи)',
            },
        ),
        migrations.CreateModel(
            name='ImmunoprophylaxisName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=350)),
            ],
            options={
                'verbose_name': 'Иммунопрофилактика (Тайтл)',
                'verbose_name_plural': 'Иммунопрофилактика (Тайтл)',
            },
        ),
        migrations.CreateModel(
            name='ImmunoprophylaxisTipical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=350)),
                ('name_two', models.CharField(default='Второе название', max_length=200)),
                ('name_three', models.CharField(default='Третье название', max_length=200)),
                ('description', models.TextField(default='Описание')),
                ('description_two', models.TextField(default='Второе описание')),
                ('description_three', models.TextField(default='Третье описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Immunoprofilactixs/')),
                ('photo_two', models.ImageField(blank=True, null=True, upload_to='Immunoprofilactixs/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата Публикации')),
            ],
            options={
                'verbose_name': 'Иммунопрофилактика (статьи)',
                'verbose_name_plural': 'Иммунопрофилактика (статьи)',
            },
        ),
    ]
