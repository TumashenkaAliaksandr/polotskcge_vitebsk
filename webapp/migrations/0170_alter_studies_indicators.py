# Generated by Django 5.0.3 on 2024-08-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0169_alter_studies_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studies',
            name='indicators',
            field=models.TextField(default='Показатели'),
        ),
    ]
