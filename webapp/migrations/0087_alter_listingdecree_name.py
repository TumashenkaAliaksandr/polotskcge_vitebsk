# Generated by Django 5.0.3 on 2024-07-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0086_listingdecree_listingdecreedesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingdecree',
            name='name',
            field=models.CharField(default='Наименование АП', max_length=350),
        ),
    ]