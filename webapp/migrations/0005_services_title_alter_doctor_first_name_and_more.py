# Generated by Django 5.0.3 on 2024-03-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services_title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Service Name', max_length=100)),
                ('description', models.TextField(default='Service Description')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Тайтл Услуги',
                'verbose_name_plural': 'Тайтл Услуги',
            },
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(default='Имя', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(default='Фамилия', max_length=100),
        ),
    ]