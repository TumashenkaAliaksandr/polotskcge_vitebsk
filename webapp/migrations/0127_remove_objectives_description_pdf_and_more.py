# Generated by Django 5.0.3 on 2024-07-30 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0126_objectives_description_pdf_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectives',
            name='description_pdf',
        ),
        migrations.RemoveField(
            model_name='objectives',
            name='description_pdf_two',
        ),
        migrations.RemoveField(
            model_name='objectives',
            name='pdf_file',
        ),
        migrations.RemoveField(
            model_name='objectives',
            name='pdf_file_two',
        ),
    ]
