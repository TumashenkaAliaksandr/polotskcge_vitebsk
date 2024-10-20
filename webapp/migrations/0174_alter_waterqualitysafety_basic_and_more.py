# Generated by Django 5.0.3 on 2024-08-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0173_alter_waterqualitysafety_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterqualitysafety',
            name='basic',
            field=models.CharField(blank=True, default='Базовый', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='waterqualitysafety',
            name='mine_well',
            field=models.CharField(blank=True, default='Шахтный колодец', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='waterqualitysafety',
            name='standart',
            field=models.CharField(blank=True, default='Стандарт', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='waterqualitysafety',
            name='standart_plus',
            field=models.CharField(blank=True, default='Стандарт Плюс', max_length=300, null=True),
        ),
    ]
