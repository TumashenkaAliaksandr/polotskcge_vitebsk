# Generated by Django 5.0.3 on 2024-11-11 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0225_laboratories_description_two'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratories',
            name='description_two',
        ),
    ]
