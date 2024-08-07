# Generated by Django 5.0.3 on 2024-07-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0077_humanresources_number_ap'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumanResourcesDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=150)),
                ('description', models.TextField(default='Описание')),
            ],
            options={
                'verbose_name': 'АП Кадровая Служба',
                'verbose_name_plural': 'АП Кадровая Служба',
            },
        ),
        migrations.AlterModelOptions(
            name='humanresources',
            options={'verbose_name': 'АП Кадровая Служба таблица', 'verbose_name_plural': 'АП Кадровая Служба таблица'},
        ),
        migrations.RemoveField(
            model_name='humanresources',
            name='description',
        ),
        migrations.RemoveField(
            model_name='humanresources',
            name='name',
        ),
    ]
