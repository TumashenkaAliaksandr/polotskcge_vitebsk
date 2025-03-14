# Generated by Django 5.0.3 on 2024-03-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_services_title_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='About Us Name One', max_length=100)),
                ('description', models.TextField(default='About Us Description One')),
                ('name_two', models.CharField(default='About Us Name Two', max_length=100)),
                ('description_two', models.TextField(default='About Us Description Two')),
                ('description_li', models.TextField(default='About Us Description Li')),
                ('description_three', models.TextField(default='About Us Description Three')),
            ],
            options={
                'verbose_name': 'Об Учреждении',
                'verbose_name_plural': 'Об Учреждении',
            },
        ),
    ]
