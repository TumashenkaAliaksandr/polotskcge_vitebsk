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
