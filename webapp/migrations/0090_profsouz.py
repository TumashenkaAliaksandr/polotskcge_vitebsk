# Generated by Django 5.0.3 on 2024-07-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0089_alter_listingdecree_name_ap_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profsouz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=350)),
                ('description', models.TextField(default='Описание - 1')),
                ('description_two', models.TextField(default='Описание - 2')),
                ('package', models.TextField(default='Состав')),
                ('number', models.CharField(default='Номер строки(ячейки в таблице)', max_length=350)),
                ('name_doctors', models.TextField(default='ФИО Доктор')),
                ('status', models.TextField(default='Должность')),
                ('phone', models.TextField(default='Телефон')),
                ('icon_telegram', models.CharField(default='bx bxl-telegram', max_length=100)),
                ('icon_facebook', models.CharField(default='bx bxl-facebook', max_length=100)),
                ('icon_vk', models.CharField(default='bx bxl-vkontakte', max_length=100)),
                ('icon_instagram', models.CharField(default='bx bxl-instagram', max_length=100)),
                ('link', models.URLField(default='https://polotskcge.by/')),
            ],
            options={
                'verbose_name': 'Профсоюз',
                'verbose_name_plural': 'Профсоюз',
            },
        ),
    ]