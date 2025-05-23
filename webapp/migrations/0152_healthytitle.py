# Generated by Django 5.0.3 on 2024-08-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0151_alter_healthy_name_taitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthyTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя Заголовка')),
                ('description', models.TextField(default='Описание')),
            ],
            options={
                'verbose_name': 'Здоровые города и поселки (ТАЙТЛ и ОПИСАНИЕ)',
                'verbose_name_plural': 'Здоровые города и поселки (ТАЙТЛ и ОПИСАНИЕ)',
            },
        ),
    ]
