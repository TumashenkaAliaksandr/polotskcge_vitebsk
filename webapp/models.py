from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    first_name = models.CharField(max_length=100, default='Имя')
    last_name = models.CharField(max_length=100, default='Фамилия')
    position = models.CharField(max_length=100, default='Doctor')
    phone = models.CharField(max_length=20, default='')
    department = models.CharField(max_length=100, default='General')
    photo = models.ImageField(upload_to='doctors/', null=True, blank=True)
    appointment_time = models.CharField(max_length=100, default='10:00 AM - 4:00 PM')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Доктора"
        verbose_name_plural = "Доктора"


class Services_title(models.Model):
    name = models.CharField(max_length=100, default='Service Name')
    description = models.TextField(default='Service Description')

    class Meta:
        verbose_name = 'Тайтл Услуги'
        verbose_name_plural = 'Тайтл Услуги'

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100, default='Service Name')
    description = models.TextField(default='Service Description')
    icon = models.ImageField(upload_to='service_icons/', null=True, blank=True)
    link = models.URLField()  # Поле для хранения ссылки

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    name = models.CharField(max_length=100, default='About Us Name One')
    description = models.TextField(default='About Us Description One')
    name_two = models.CharField(max_length=100, default='About Us Name Two')
    description_two = models.TextField(default='About Us Description Two')
    name_li_one = models.CharField(max_length=100, default='About Us Name Li-One')
    name_li_two = models.CharField(max_length=100, default='About Us Name Li-Two')
    name_li_three = models.CharField(max_length=100, default='About Us Name Li-Three')
    name_li_four = models.CharField(max_length=100, default='About Us Name Li-Four')
    name_li_five = models.CharField(max_length=100, default='About Us Name Li-Five')
    description_three = models.TextField(default='About Us Description Three')
    photo = models.ImageField(upload_to='about_us/', null=True, blank=True)

    class Meta:
        verbose_name = 'Об Учреждении'
        verbose_name_plural = 'Об Учреждении'

    def __str__(self):
        return self.name


class Researches(models.Model):
    name = models.CharField(max_length=100, default='Researches Name One')
    description = models.TextField(default='Researches Description One')
    name_two = models.CharField(max_length=100, default='Researches Name Two')
    description_two = models.TextField(default='Researches Description Two')
    name_three = models.CharField(max_length=100, default='Researches Name Three')
    description_three = models.TextField(default='Researches Description Three')
    name_four = models.CharField(max_length=100, default='Researches Name Four')
    description_four = models.TextField(default='Researches Description Four')
    photo = models.ImageField(upload_to='researches/', null=True, blank=True)

    class Meta:
        verbose_name = 'Блок Иновации'
        verbose_name_plural = 'Блок Иновации'

    def __str__(self):
        return self.name
