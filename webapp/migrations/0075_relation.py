# Generated by Django 5.0.3 on 2024-07-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0074_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=150)),
                ('description', models.TextField(default='Описание')),
            ],
            options={
                'verbose_name': 'АП в отношении граждан',
                'verbose_name_plural': 'АП в отношении граждан',
            },
        ),
    ]
