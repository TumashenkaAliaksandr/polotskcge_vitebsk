# Generated by Django 5.0.3 on 2024-05-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_remove_previewnews_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelnews',
            name='is_main_days_health',
            field=models.BooleanField(blank=True, default=False, verbose_name='Единые дни здоровья'),
        ),
        migrations.AddField(
            model_name='modelnews',
            name='is_main_measures',
            field=models.BooleanField(blank=True, default=False, verbose_name='Профилактитческие мероприятия'),
        ),
    ]
