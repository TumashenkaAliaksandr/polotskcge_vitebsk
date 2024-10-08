# Generated by Django 5.0.3 on 2024-07-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0083_alter_accounting_name_ap_alter_accounting_number_ap_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnionDesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл', max_length=150)),
                ('description', models.TextField(default='Описание')),
            ],
            options={
                'verbose_name': 'АП Профсоюз',
                'verbose_name_plural': 'АП Профсоюз',
            },
        ),
        migrations.AlterModelOptions(
            name='accountingdesc',
            options={'verbose_name': 'АП Бухгалтерия тайтл', 'verbose_name_plural': 'АП Бухгалтерия тайтл'},
        ),
    ]
