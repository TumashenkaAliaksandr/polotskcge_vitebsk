# Generated by Django 5.0.3 on 2024-10-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0212_monitoringplanarkhive'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pdf_file', models.FileField(upload_to='city_documents/')),
            ],
            options={
                'verbose_name': 'Города/Поселок - (страница прикрепить ПДФ, архив)',
                'verbose_name_plural': 'Города/Поселок - (страница прикрепить ПДФ, архив)',
            },
        ),
    ]