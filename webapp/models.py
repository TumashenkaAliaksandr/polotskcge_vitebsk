from ckeditor.fields import RichTextField
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


class Book_complaint(models.Model):
    """This Model for Book_complaint block on the main page"""

    name = models.CharField(max_length=100, default='Book Name')
    description = models.TextField(default='Book Description')

    class Meta:
        verbose_name = 'Книга жалоб и предложений'
        verbose_name_plural = 'Книга жалоб и предложений'

    def __str__(self):
        return self.name

class EducationalResource(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = RichTextField(verbose_name="Описание")
    pdf_file = models.FileField(upload_to='pdfs/', verbose_name="Прикрепить PDF")
    icon_class = models.CharField(max_length=100, default='fas fa-file-pdf')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Образовательный ресурс"
        verbose_name_plural = "Образовательные ресурсы"
        ordering = ['-pub_date']


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


class GeneralInfo(models.Model):
    title = models.CharField(max_length=100, default='Тайтл')
    description = RichTextField(max_length=200, default='Описание')

    class Meta:
        verbose_name = 'Заголовок и описание для Часы Приёма'
        verbose_name_plural = 'Заголовок и описание для Часы Приёма'

    def __str__(self):
        return self.title

class ReceptionHours(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='Имя и Отчество')
    family_name = models.CharField(max_length=100, default='Фамилия')
    office = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    reception_time = models.CharField(max_length=100, default='Часы приёма')
    # general_info = models.OneToOneField(GeneralInfo, on_delete=models.CASCADE, related_name='reception_hours')
    general_info = models.ForeignKey(GeneralInfo, on_delete=models.CASCADE, related_name='reception_hours',
                                        blank=True, null=True, default='Основная Инф')

    class Meta:
        verbose_name = 'Часы приема'
        verbose_name_plural = 'Часы приема'

    def __str__(self):
        return self.name


class HotlineHours(models.Model):
    name = models.CharField(max_length=100, default='Фамилия Имя и Отчество')
    post = models.CharField(max_length=100, default='Должность')
    phone = models.CharField(max_length=100)
    reception_time = models.CharField(max_length=100, default='Время проведения прямой линии')
    date_hotline = models.CharField(max_length=100, default='Дата Проведения прям линии')

    class Meta:
        verbose_name = 'Прямая линия'
        verbose_name_plural = 'Прямая линия'

    def __str__(self):
        return self.name

class HotlineHours_Title(models.Model):
    name = models.CharField(max_length=100, default='Прямая Телефонная Линия')
    description = models.CharField(max_length=300, default='График проведения "прямой телефонной линии" в Государственном учреждении "Полоцкий зональный центр гигиены и эпидемиологии"')

    class Meta:
        verbose_name = 'Прямая линия тайтл и описание'
        verbose_name_plural = 'Прямая линия тайтл и описание'

    def __str__(self):
        return self.name


class HotlineHours_Title_desc(models.Model):
    name = models.CharField(max_length=300, default='Порядок проведения')
    description = models.CharField(max_length=3000, default='Описание проведения')

    class Meta:
        verbose_name = 'Порядок проведения тайтл и описание'
        verbose_name_plural = 'Порядок проведения тайтл и описание'

    def __str__(self):
        return self.name


class Electronic_appeals_Title_desc(models.Model):
    name = models.CharField(max_length=300, default='Порядок проведения')
    description = models.CharField(max_length=3000, default='Описание проведения')

    class Meta:
        verbose_name = 'Электронные Обращения тайтл и описание'
        verbose_name_plural = 'Электронные Обращения тайтл и описание'

    def __str__(self):
        return self.name

class Up_Organ_inf(models.Model):
    name = models.CharField(max_length=300, default='Телефон горячей линии')
    description = models.CharField(max_length=3000, default='Время работы')

    class Meta:
        verbose_name = 'Информация (низ стр) Вышестоящий Орган'
        verbose_name_plural = 'Информация (низ стр) Вышестоящий Орган'

    def __str__(self):
        return self.name


class Expertise(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    description = models.CharField(max_length=3000, default='Первое большое описание')
    description_two = models.CharField(max_length=3000, default='Второе описание')
    description_three = models.CharField(max_length=3000, default='Третье описание')

    class Meta:
        verbose_name = 'Экспертиза'
        verbose_name_plural = 'Экспертиза'

    def __str__(self):
        return self.name


class Organ_Title_desc(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    description = models.CharField(max_length=3000, default='Описание')

    class Meta:
        verbose_name = 'Вышестоящий орган тайтл и описание'
        verbose_name_plural = 'Вышестоящий орган тайтл и описание'

    def __str__(self):
        return self.name


class Up_Organ(models.Model):
    name = models.CharField(max_length=100, default='Фамилия Имя и Отчество')
    post = models.CharField(max_length=100, default='Должность')
    phone = models.CharField(max_length=100)
    reception_time = models.CharField(max_length=200, default='Время Приема')

    class Meta:
        verbose_name = 'Вышестоящий орган данные'
        verbose_name_plural = 'Вышестоящий орган данные'

    def __str__(self):
        return self.name



class Question(models.Model):
    question_text = models.CharField(max_length=255, default='вопрос')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', blank=True, null=True)  # Added publication date field

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.answer_text


class Question_Ansver_title(models.Model):

    name = models.CharField(max_length=255, default='Заголовок')
    description = RichTextField(max_length=200, default='Описание')

    class Meta:
        verbose_name = 'Заголовок и Описание Ответов'
        verbose_name_plural = 'Заголовок и Описание Ответов'

    def __str__(self):
        return self.name


class Zoj(models.Model):
    name = models.CharField(max_length=100, default='Zoj Us Name One')
    description = models.TextField(default='Zoj Us Description One')
    name_two = models.CharField(max_length=100, default='Zoj Us Name Two')
    description_two = models.TextField(default='Zoj Us Description Two')
    name_li_one = models.CharField(max_length=150, default='Zoj Us Name Li-One')
    name_li_two = models.CharField(max_length=150, default='Zoj Us Name Li-Two')
    name_li_three = models.CharField(max_length=150, default='Zoj Us Name Li-Three')
    name_li_four = models.CharField(max_length=150, default='Zoj Us Name Li-Four')
    name_li_five = models.CharField(max_length=150, default='Zoj Us Name Li-Five')
    description_three = models.TextField(default='Zoj Us Description Three')
    photo = models.ImageField(upload_to='Zoj/', null=True, blank=True)
    photo_two = models.ImageField(upload_to='Zoj/', null=True, blank=True)
    icon_class = models.CharField(max_length=100, default='bi bi-check-circle')  # Для основного описания
    icon_class_li_one = models.CharField(max_length=100, default='bi bi-check-circle')  # Для первого элемента списка
    icon_class_li_two = models.CharField(max_length=100, default='bi bi-check-circle')  # Для второго элемента списка
    icon_class_li_three = models.CharField(max_length=100, default='bi bi-check-circle')  # Для третьего элемента списка
    icon_class_li_four = models.CharField(max_length=100, default='bi bi-check-circle')  # Для четвертого элемента списка
    icon_class_li_five = models.CharField(max_length=100, default='bi bi-check-circle')  # Для пятого элемента списка

    class Meta:
        verbose_name = 'Здоровый Образ Жизни'
        verbose_name_plural = 'Здоровый Образ Жизни'

    def __str__(self):
        return self.name
