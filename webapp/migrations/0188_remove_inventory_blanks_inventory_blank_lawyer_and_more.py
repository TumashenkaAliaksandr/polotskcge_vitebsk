# Generated by Django 5.0.3 on 2024-09-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0187_inventory_blanks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='blanks',
        ),
        migrations.AddField(
            model_name='inventory',
            name='blank_lawyer',
            field=models.TextField(default='Бланк для Юр лица'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='blanks_civilnyi',
            field=models.TextField(default='Бланк для Физ лица'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='name_for_blanks',
            field=models.CharField(default='Тайтл для бланков', max_length=350),
        ),
    ]