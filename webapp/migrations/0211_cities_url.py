# Generated by Django 5.0.3 on 2024-10-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0210_monitoringplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]