# Generated by Django 5.0.3 on 2024-08-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0146_alter_quarantine_desc_two'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarantine',
            name='desc',
            field=models.TextField(blank=True, default='Описание под тайтл'),
        ),
        migrations.AlterField(
            model_name='quarantine',
            name='desc_two',
            field=models.TextField(blank=True, default='СКП'),
        ),
    ]