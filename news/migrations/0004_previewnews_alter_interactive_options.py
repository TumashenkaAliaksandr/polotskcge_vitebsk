# Generated by Django 5.0.3 on 2024-04-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_interactive_description_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название превью')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='news_preview_photos/', verbose_name='Фотографии Превью Новостей')),
            ],
            options={
                'verbose_name': 'Превью новостей',
                'verbose_name_plural': 'Превью новостей',
            },
        ),
        migrations.AlterModelOptions(
            name='interactive',
            options={'verbose_name': 'Интерактитвная новость', 'verbose_name_plural': 'Интерактитвная новость'},
        ),
    ]
