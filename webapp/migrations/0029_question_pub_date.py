# Generated by Django 5.0.3 on 2024-05-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0028_alter_generalinfo_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата Публикации'),
        ),
    ]