# Generated by Django 5.0.3 on 2024-07-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0110_alter_controlnadzortipical_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlnadzortipical',
            name='name_typical',
            field=models.CharField(default='Тайтл', max_length=350),
        ),
        migrations.AlterField(
            model_name='controlnadzortipical',
            name='name',
            field=models.CharField(default='Тайтл для админки', max_length=350),
        ),
    ]
