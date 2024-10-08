# Generated by Django 5.0.3 on 2024-08-04 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0149_resolution'),
    ]

    operations = [
        migrations.CreateModel(
            name='Healthy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('name_taitle', models.CharField(max_length=100, verbose_name='Имя')),
                ('pdf_file', models.FileField(upload_to='pdfs/', verbose_name='Прикрепить PDF')),
                ('icon_class', models.CharField(default='fas fa-file-pdf', max_length=100)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата Публикации')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Здоровые города и поселки',
                'verbose_name_plural': 'Здоровые города и поселки',
                'ordering': ['-pub_date'],
            },
        ),
    ]
