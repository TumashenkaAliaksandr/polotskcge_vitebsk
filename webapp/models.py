from django.db import models
from django.contrib.auth.models import User


class Logo(models.Model):
    """This is main haider logo model"""

    name = models.CharField(max_length=100, default='Logo Name')
    icon = models.ImageField(upload_to='logo/', null=True, blank=True)
    link = models.URLField()  # Поле для хранения ссылки

    class Meta:
        verbose_name = 'Лого на Главной'
        verbose_name_plural = 'Лого на Главной'

    def __str__(self):
        return self.name


class Featured(models.Model):
    """This Model for Featured block on the main page"""

    name = models.CharField(max_length=100, default='Featured Name')
    description = models.TextField(default='Featured Description')
    link = models.URLField()  # Поле для хранения ссылки
    icon_class = models.CharField(max_length=100, default='fas fa-heartbeat')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return self.name


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


from django.db import models

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
    icon_class = models.CharField(max_length=100, default='bi bi-check-circle')  # Для основного описания
    icon_class_li_one = models.CharField(max_length=100, default='bi bi-check-circle')  # Для первого элемента списка
    icon_class_li_two = models.CharField(max_length=100, default='bi bi-check-circle')  # Для второго элемента списка
    icon_class_li_three = models.CharField(max_length=100, default='bi bi-check-circle')  # Для третьего элемента списка
    icon_class_li_four = models.CharField(max_length=100, default='bi bi-check-circle')  # Для четвертого элемента списка
    icon_class_li_five = models.CharField(max_length=100, default='bi bi-check-circle')  # Для пятого элемента списка

    class Meta:
        verbose_name = 'Об Учреждении'
        verbose_name_plural = 'Об Учреждении'

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name


from django.db import models

class Researches(models.Model):
    name = models.CharField(max_length=100, default='Researches Name One')
    description = models.TextField(default='Researches Description One')
    icon_class = models.CharField(max_length=100, default='bx bxs-flask')  # Иконка для первого описания
    name_two = models.CharField(max_length=100, default='Researches Name Two')
    description_two = models.TextField(default='Researches Description Two')
    icon_class_two = models.CharField(max_length=100, default='bx bxs-flask')  # Иконка для второго описания
    name_three = models.CharField(max_length=100, default='Researches Name Three')
    description_three = models.TextField(default='Researches Description Three')
    icon_class_three = models.CharField(max_length=100, default='bx bxs-flask')  # Иконка для третьего описания
    name_four = models.CharField(max_length=100, default='Researches Name Four')
    description_four = models.TextField(default='Researches Description Four')
    icon_class_four = models.CharField(max_length=100, default='bx bxs-flask')  # Иконка для четвертого описания
    photo = models.ImageField(upload_to='researches/', null=True, blank=True)

    class Meta:
        verbose_name = 'Блок Иновации'
        verbose_name_plural = 'Блок Иновации'

    def __str__(self):
        return self.name


class ReceptionHours(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='Имя и Отчество')
    family_name = models.CharField(max_length=100, default='Фамилия')
    office = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    reception_time = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Часы приема'
        verbose_name_plural = 'Часы приема'

    def __str__(self):
        return self.name

