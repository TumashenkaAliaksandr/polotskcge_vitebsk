# Generated by Django 5.0.3 on 2024-08-30 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0174_alter_waterqualitysafety_basic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LaboratoryFruitVegetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('desc', models.CharField(default='Описание', max_length=500)),
                ('paket', models.TextField(default='Пакет исследований')),
                ('cost', models.CharField(blank=True, default='Цена', max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Лабораторные исследования плодоовощной продукции',
                'verbose_name_plural': 'Лабораторные исследования плодоовощной продукции',
            },
        ),
    ]