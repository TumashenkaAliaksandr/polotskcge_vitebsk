# Generated by Django 5.0.3 on 2024-07-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0125_objectives'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectives',
            name='description_pdf',
            field=models.TextField(default='Описание PDF'),
        ),
        migrations.AddField(
            model_name='objectives',
            name='description_pdf_two',
            field=models.TextField(default='Описание PDF'),
        ),
    ]