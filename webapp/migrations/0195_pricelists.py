# Generated by Django 5.0.3 on 2024-09-08 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0194_ourpartners_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceLists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=100)),
                ('description', models.TextField(default='Description')),
                ('link', models.URLField(blank=True)),
                ('icon_class', models.CharField(default='fas fa-heartbeat', max_length=100)),
                ('add_file', models.FileField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Прейскуранты',
                'verbose_name_plural': 'Прейскуранты',
            },
        ),
    ]
