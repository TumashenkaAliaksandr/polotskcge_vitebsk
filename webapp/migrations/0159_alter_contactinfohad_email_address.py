# Generated by Django 5.0.3 on 2024-08-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0158_alter_contactinfohad_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfohad',
            name='email_address',
            field=models.CharField(default='polotzk_hyg@vitebsk.by', max_length=70),
        ),
    ]
