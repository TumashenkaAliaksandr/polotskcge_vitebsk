# Generated by Django 5.0.3 on 2024-08-25 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0159_alter_contactinfohad_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfohad',
            name='phone_number',
            field=models.CharField(default='+80214493168', max_length=25),
        ),
    ]