# Generated by Django 5.0.3 on 2024-07-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0104_disinsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisinfectionDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл для админки', max_length=350)),
                ('name_main', models.CharField(default='Тайтл', max_length=350)),
                ('description', models.TextField(default='Описание')),
                ('description_two', models.TextField(default='Описание 2')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Disinfection/')),
            ],
            options={
                'verbose_name': 'Дезинфекция описание',
                'verbose_name_plural': 'Дезинфекция описание',
            },
        ),
    ]
