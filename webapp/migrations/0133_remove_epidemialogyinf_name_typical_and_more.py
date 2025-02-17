# Generated by Django 5.0.3 on 2024-08-01 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0132_epidemialogyinf_epidemialogyname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='epidemialogyinf',
            name='name_typical',
        ),
        migrations.RemoveField(
            model_name='epidemialogyname',
            name='name_typical',
        ),
        migrations.RemoveField(
            model_name='epidemialogysinglename',
            name='name_typical',
        ),
        migrations.AlterField(
            model_name='epidemialogyinf',
            name='name',
            field=models.CharField(default='Тайтл', max_length=350),
        ),
        migrations.AlterField(
            model_name='epidemialogyname',
            name='name',
            field=models.CharField(default='Тайтл', max_length=350),
        ),
        migrations.AlterField(
            model_name='epidemialogysinglename',
            name='name',
            field=models.CharField(default='Тайтл', max_length=350),
        ),
    ]
