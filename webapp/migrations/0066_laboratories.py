# Generated by Django 5.0.3 on 2024-06-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0065_laboratory_name_three'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=100)),
                ('description', models.TextField(default='Первое описание')),
                ('icon_class', models.CharField(default='bx bxs-flask', max_length=100)),
                ('name_two', models.CharField(default='Второе Имя', max_length=100)),
                ('description_two', models.TextField(default='Второе Описание')),
                ('icon_class_two', models.CharField(default='bx bxs-flask', max_length=100)),
                ('name_three', models.CharField(default='Третье Имя', max_length=100)),
                ('description_three', models.TextField(default='Третье Описание')),
                ('icon_class_three', models.CharField(default='bx bxs-flask', max_length=100)),
                ('name_four', models.CharField(default='Четвертое Имя', max_length=100)),
                ('description_four', models.TextField(default='Четвертое Описание')),
                ('icon_class_four', models.CharField(default='bx bxs-flask', max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Laboratory/')),
            ],
            options={
                'verbose_name': 'Лабораторные услуги (2ая половина)',
                'verbose_name_plural': 'Лабораторные услуги (2ая половина)',
            },
        ),
    ]