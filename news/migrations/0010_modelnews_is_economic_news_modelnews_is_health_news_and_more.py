# Generated by Django 5.0.3 on 2024-05-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_modelnews_is_nature_news_modelnews_is_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelnews',
            name='is_economic_news',
            field=models.BooleanField(blank=True, default=False, verbose_name='Новости экономики'),
        ),
        migrations.AddField(
            model_name='modelnews',
            name='is_health_news',
            field=models.BooleanField(blank=True, default=False, verbose_name='Новости о здоровье'),
        ),
        migrations.AddField(
            model_name='modelnews',
            name='is_main_news',
            field=models.BooleanField(blank=True, default=False, verbose_name='Важное'),
        ),
        migrations.AddField(
            model_name='modelnews',
            name='is_sport_news',
            field=models.BooleanField(blank=True, default=False, verbose_name='Новости спорта'),
        ),
    ]
