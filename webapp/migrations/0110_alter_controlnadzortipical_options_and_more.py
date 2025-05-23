# Generated by Django 5.0.3 on 2024-07-23 11:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0109_rename_controlnadzor_controlnadzortipical'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='controlnadzortipical',
            options={'verbose_name': 'Контрольно надзорная деятельность Типичные нарушения(таблица)', 'verbose_name_plural': 'Контрольно надзорная деятельность Типичные нарушения(таблица)'},
        ),
        migrations.AddField(
            model_name='controlnadzortipical',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата Публикации'),
        ),
    ]
