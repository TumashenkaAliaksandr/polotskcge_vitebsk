# Generated by Django 5.0.3 on 2024-10-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0211_cities_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoringPlanArkhive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл для админки', max_length=350)),
                ('name_main', models.CharField(default='Тайтл', max_length=350)),
                ('description', models.TextField(default='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='MonitoringPlanArkhive/')),
            ],
            options={
                'verbose_name': 'План Мониторинга Архив',
                'verbose_name_plural': 'План Мониторинга Архив',
            },
        ),
    ]
