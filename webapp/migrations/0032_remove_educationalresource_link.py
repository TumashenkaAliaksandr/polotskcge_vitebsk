# Generated by Django 5.0.3 on 2024-05-27 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0031_educationalresource_icon_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalresource',
            name='link',
        ),
    ]