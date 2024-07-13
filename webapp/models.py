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


class AnticorrTitle(models.Model):
    """This Model for Anticorr Title block on the anticorruptions page"""

    name = models.CharField(max_length=200, default='Тайтл Анткоррупция')
    desc_anticorr = models.CharField(max_length=500, default='Описание под тайтл Анткоррупция')

    class Meta:
        verbose_name = 'Антикоррупция тайтл'
        verbose_name_plural = 'Антикоррупция тайтл'

    def __str__(self):
        return self.name


class Anticorr(models.Model):
    """This Model for Anticorr block on the anticorruptions page"""

    name = models.CharField(max_length=300, default='Тайтл в карточку Анткоррупция')
    description = models.TextField(default='Featured Description')
    link = models.URLField()  # Поле для хранения ссылки
    icon_class = models.CharField(max_length=100, default='fas fa-heartbeat')

    class Meta:
        verbose_name = 'Антикоррупция'
        verbose_name_plural = 'Антикоррупция'

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


class MaintenanceSchedule(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    description = models.CharField(max_length=3000, default='Большое описание')

    class Meta:
        verbose_name = 'Порядок и Сроки Обжалования'
        verbose_name_plural = 'Порядок и Сроки Обжалования'

    def __str__(self):
        return self.name


class Duties(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    description = models.CharField(max_length=7000, default='Большое описание')

    class Meta:
        verbose_name = 'Права и обязанности'
        verbose_name_plural = 'Права и обязанности'

    def __str__(self):
        return self.name


class Vacancies(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    vacancy = models.CharField(max_length=7000, default='Вакансия 1')
    vacancy_two = models.CharField(max_length=7000, default='Вакансия 2')
    vacancy_three = models.CharField(max_length=7000, default='Вакансия 3')

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name


class MainAppeals(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    name_two = models.CharField(max_length=300, default='Тайтл 2')
    name_three = models.CharField(max_length=300, default='Тайтл 3')
    appeals_desc = models.CharField(max_length=300, default='Описание под тайтл')
    appeals_desc_two = models.CharField(max_length=7000, default='Описание')
    appeals_desc_three = models.CharField(max_length=7000, default='Описание 2')
    appeals_desc_four = models.CharField(max_length=7000, default='Описание 3')

    class Meta:
        verbose_name = 'Обращения главная'
        verbose_name_plural = 'Обращения главная'

    def __str__(self):
        return self.name


class NormativeDocuments(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    normative_desc = models.CharField(max_length=300, default='Описание под тайтл')

    class Meta:
        verbose_name = 'Нормативные документы'
        verbose_name_plural = 'Нормативные документы'

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


class Laboratory(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')
    name_two = models.CharField(max_length=200, default='Второе название')
    name_three = models.CharField(max_length=200, default='Третье название')
    description_two = models.TextField(default='Второе описание')
    name_li_one = models.CharField(max_length=200, default='Первое имя с тегом li')
    name_li_two = models.CharField(max_length=200, default='Второе имя с тегом li')
    name_li_three = models.CharField(max_length=200, default='Третье имя с тегом li')
    name_li_four = models.CharField(max_length=200, default='Четвертое имя с тегом li')
    name_li_five = models.CharField(max_length=200, default='Пятое имя с тегом li')
    name_li_six = models.CharField(max_length=200, default='Шестое имя с тегом li')
    description_three = models.TextField(default='Третье описание')
    photo = models.ImageField(upload_to='laboratory/', null=True, blank=True)
    icon_class = models.CharField(max_length=100, default='bi bi-check-circle')  # Для основного описания
    icon_class_li_one = models.CharField(max_length=100, default='bi bi-check-circle')  # Для первого элемента списка
    icon_class_li_two = models.CharField(max_length=100, default='bi bi-check-circle')  # Для второго элемента списка
    icon_class_li_three = models.CharField(max_length=100, default='bi bi-check-circle')  # Для третьего элемента списка
    icon_class_li_four = models.CharField(max_length=100, default='bi bi-check-circle')  # Для четвертого элемента списка
    icon_class_li_five = models.CharField(max_length=100, default='bi bi-check-circle')  # Для пятого элемента списка
    icon_class_li_six = models.CharField(max_length=100, default='bi bi-check-circle')  # Для пятого элемента списка

    class Meta:
        verbose_name = 'Лабораторные услуги'
        verbose_name_plural = 'Лабораторные услуги'

    def __str__(self):
        return self.name


class Laboratories(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')
    photo = models.ImageField(upload_to='Laboratory/', null=True, blank=True)

    class Meta:
        verbose_name = 'Лабораторные услуги (2ая половина)'
        verbose_name_plural = 'Лабораторные услуги (2ая половина)'

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    description_three = models.TextField(default='Описание 3')

    class Meta:
        verbose_name = 'АП Регистрация'
        verbose_name_plural = 'АП Регистрация'

    def __str__(self):
        return self.name


class Relation(models.Model):
    """Model Relation"""
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = 'АП в отношении граждан'
        verbose_name_plural = 'АП в отношении граждан'

    def __str__(self):
        return self.name


class HumanResourcesDesc(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = 'АП Кадровая Служба'
        verbose_name_plural = 'АП Кадровая Служба'

    def __str__(self):
        return self.name


class HumanResources(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    number_ap = models.CharField(max_length=300, default='Номер административной процедуры')
    name_ap = models.CharField(max_length=300, default='Наименование административной процедуры')
    doc_ap = models.CharField(max_length=300, default='Документы и (или) сведения АП')
    size_ap = models.CharField(max_length=300, default='Размер Платы взымаемой при АП')

    class Meta:
        verbose_name = 'АП Кадровая Служба таблица'
        verbose_name_plural = 'АП Кадровая Служба таблица'

    def __str__(self):
        return self.number_ap


class AccountingDesc(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = 'АП Бухгалтерия тайтл'
        verbose_name_plural = 'АП Бухгалтерия тайтл'

    def __str__(self):
        return self.name


class Accounting(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    number_ap = models.CharField(max_length=500, default='Номер административной процедуры')
    name_ap = models.CharField(max_length=500, default='Наименование административной процедуры')
    doc_ap = models.TextField(default='Документы и (или) сведения АП')
    size_ap = models.CharField(max_length=500, default='Размер Платы взымаемой при АП')
    date_ap = models.CharField(max_length=500, default='Сроки выполнения АП')

    class Meta:
        verbose_name = 'АП Кадровая Служба таблица Бухгалтерия'
        verbose_name_plural = 'АП Кадровая Служба таблица Бухгалтерия'

    def __str__(self):
        return self.number_ap


class UnionDesc(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = 'АП Профсоюз'
        verbose_name_plural = 'АП Профсоюз'

    def __str__(self):
        return self.name


class Union(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    number_ap = models.CharField(max_length=500, default='Номер профсоюзной процедуры')
    name_ap = models.CharField(max_length=500, default='Наименование профсоюзной процедуры')
    doc_ap = models.TextField(default='Документы и (или) сведения АП')
    size_ap = models.CharField(max_length=500, default='Размер Платы взымаемой при АП')
    date_ap = models.CharField(max_length=500, default='Сроки выполнения АП')

    class Meta:
        verbose_name = 'АП Профсоюз таблица'
        verbose_name_plural = 'АП Профсоюз таблица'

    def __str__(self):
        return self.number_ap


class ListingDecreeDesc(models.Model):
    name = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = 'АП Указ (в отношении граждан)'
        verbose_name_plural = 'АП Указ (в отношении граждан)'

    def __str__(self):
        return self.name


class ListingDecree(models.Model):
    name = models.CharField(max_length=350, default='Наименование АП')
    number_ap = models.CharField(max_length=100, default='Номер профсоюзной процедуры')
    name_ap = models.CharField(max_length=1000, default='Гос орган для обращения')
    doc_ap = models.TextField(default='Документы и (или) сведения')
    size_ap = models.CharField(max_length=500, default='Максимальный срок выполнения')
    date_ap = models.CharField(max_length=500, default='Сроки действия')

    class Meta:
        verbose_name = 'АП указ таблица'
        verbose_name_plural = 'АП указ таблица'

    def __str__(self):
        return self.number_ap


class Profsouz(models.Model):
    name = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание - 1')
    description_two = models.TextField(default='Описание - 2')
    number = models.CharField(max_length=350, default='Номер строки(ячейки в таблице)')
    name_doctors = models.TextField(default='ФИО Доктор')
    status = models.TextField(default='Должность')
    phone = models.TextField(default='Телефон')

    class Meta:
        verbose_name = 'О центре Профсоюз таблицы с сотрудниками'
        verbose_name_plural = 'О центре Профсоюз таблицы с сотрудниками'

    def __str__(self):
        return self.name


class ProfsouzTwo(models.Model):

    name = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание - 1')
    description_two = models.TextField(default='Описание - 2')
    number = models.CharField(max_length=350, default='Номер строки(ячейки в таблице)')
    name_doctors = models.TextField(default='ФИО Доктор')
    status = models.TextField(default='Должность')
    phone = models.TextField(default='Телефон')

    class Meta:
        verbose_name = 'О центре Профсоюз таблицы с сотрудниками (таблица 2)'
        verbose_name_plural = 'О центре Профсоюз таблицы с сотрудниками (таблица 2)'

    def __str__(self):
        return self.name


class ProfsouzDesc(models.Model):
    name = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание - 1')
    description_two = models.TextField(default='Описание - 2')
    package = models.TextField(default='Состав')

    class Meta:
        verbose_name = 'О центре Профсоюз верхнее описание'
        verbose_name_plural = 'О центре Профсоюз верхнее описание'

    def __str__(self):
        return self.name


class ProfsouzDescOne(models.Model):
    name = models.CharField(max_length=350, default='Тайтл')
    name_main = models.CharField(max_length=350, default='Тайтл на страницу')
    description = models.TextField(default='Описание - 1')
    description_two = models.TextField(default='Описание - 2')
    package = models.TextField(default='Состав')

    class Meta:
        verbose_name = 'О центре Профсоюз описание таблицы'
        verbose_name_plural = 'О центре Профсоюз таблицы'

    def __str__(self):
        return self.name


class ProfsouzIcons(models.Model):
    name = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание Два')
    icon_telegram = models.CharField(max_length=100, default='bx bxl-telegram')
    link_telegram = models.URLField(max_length=200, default='https://telegram.com')
    icon_facebook = models.CharField(max_length=100, default='bx bxl-facebook')
    link_facebook = models.URLField(max_length=200, default='https://facebook.com')
    icon_vk = models.CharField(max_length=100, default='bx bxl-vkontakte')
    link_vk = models.URLField(max_length=200, default='https://vk.com')
    icon_instagram = models.CharField(max_length=100, default='bx bxl-instagram')
    link_instagram = models.URLField(max_length=200, default='https://instagram.com')

    class Meta:
        verbose_name = 'О центре Профсоюз Иконки'
        verbose_name_plural = 'О центре Профсоюз Иконки'

    def __str__(self):
        return self.name


class Disinfection(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')

    class Meta:
        verbose_name = 'Дезинфекция главное'
        verbose_name_plural = 'Дезинфекция главное'

    def __str__(self):
        return self.name


class Deratization(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    photo = models.ImageField(upload_to='Deratization/', null=True, blank=True)

    class Meta:
        verbose_name = 'Дератизация описание'
        verbose_name_plural = 'Дератизация описание'

    def __str__(self):
        return self.name


class Disinsection(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    photo = models.ImageField(upload_to='Disinsection/', null=True, blank=True)

    class Meta:
        verbose_name = 'Дезинсекция описание'
        verbose_name_plural = 'Дезинсекция описание'

    def __str__(self):
        return self.name


class DisinfectionDesc(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    photo = models.ImageField(upload_to='Disinfection/', null=True, blank=True)

    class Meta:
        verbose_name = 'Дезинфекция описание'
        verbose_name_plural = 'Дезинфекция описание'

    def __str__(self):
        return self.name
