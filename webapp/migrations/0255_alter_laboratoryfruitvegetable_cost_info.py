# Generated by Django 5.0.3 on 2025-05-10 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0254_laboratoryfruitvegetable_cost_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratoryfruitvegetable',
            name='cost_info',
            field=models.TextField(default='Цена указана по состоянию на:', max_length=500),
        ),
    ]
