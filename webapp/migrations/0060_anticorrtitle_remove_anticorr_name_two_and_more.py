# Generated by Django 5.0.3 on 2024-06-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0059_alter_anticorr_name_alter_anticorr_name_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnticorrTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Тайтл Анткоррупция', max_length=200)),
                ('desc_anticorr', models.CharField(default='Описание под тайтл Анткоррупция', max_length=500)),
            ],
            options={
                'verbose_name': 'Антикоррупция тайтл',
                'verbose_name_plural': 'Антикоррупция тайтл',
            },
        ),
        migrations.RemoveField(
            model_name='anticorr',
            name='name_two',
        ),
        migrations.AlterField(
            model_name='anticorr',
            name='name',
            field=models.CharField(default='Тайтл в карточку Анткоррупция', max_length=300),
        ),
    ]