# Generated by Django 5.0.3 on 2024-06-29 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0069_remove_laboratories_icon_class_four_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laboratories',
            old_name='description_icon',
            new_name='description_services',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='description_five',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='description_four',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='description_seven',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='description_six',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='description_three',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='description_two',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='icon_class',
        ),
        migrations.RemoveField(
            model_name='laboratories',
            name='icon_class_two',
        ),
    ]