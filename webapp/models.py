import django
from django.utils import timezone
from tinymce.models import HTMLField
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
        verbose_name = '❤️ Избранное(первый блок на гл.,стр)'
        verbose_name_plural = '❤️ Избранное (первый блок на гл.,стр)'

    def __str__(self):
        return self.name


class PriceLists(models.Model):
    """This Model for Price Lists block on the main page"""

    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')
    link = models.URLField(blank=True)  # Поле для хранения ссылки
    icon_class = models.CharField(max_length=100, default='fas fa-file-invoice')
    add_file = models.FileField(blank=True)

    class Meta:
        verbose_name = '🔖 Прейскуранты'
        verbose_name_plural = '🔖 Прейскуранты'

    def __str__(self):
        return self.name


class PriceListsFiz(models.Model):
    """This Model for Price Lists Fiz block on the main page"""

    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')
    link = models.URLField(blank=True)  # Поле для хранения ссылки
    icon_class = models.CharField(max_length=100, default='fas fa-file-invoice')
    add_file = models.FileField(blank=True)

    class Meta:
        verbose_name = '🗃️ Доки для Физ лиц (нижний блок перед ерип)'
        verbose_name_plural = '🗃️ Доки для Физ лиц (нижний блок перед ерип)'

    def __str__(self):
        return self.name


class AnticorrTitle(models.Model):
    """This Model for Anticorr Title block on the anticorruptions page"""

    name = models.CharField(max_length=200, default='Тайтл Анткоррупция')
    desc_anticorr = models.CharField(max_length=500, default='Описание под тайтл Анткоррупция')

    class Meta:
        verbose_name = '👮📌 Антикоррупция ТАЙТЛ  🇹 '
        verbose_name_plural = '👮📌 Антикоррупция ТАЙТЛ  🇹 '

    def __str__(self):
        return self.name


class Anticorr(models.Model):
    """This Model for Anticorr block on the anticorruptions page"""

    name = models.CharField(max_length=300, default='Тайтл в карточку Анткоррупция')
    description = models.TextField(default='Featured Description')
    link = models.URLField()  # Поле для хранения ссылки
    icon_class = models.CharField(max_length=100, default='fas fa-heartbeat')

    class Meta:
        verbose_name = '👮📌 Антикоррупция (блоки PDF верх стр.)'
        verbose_name_plural = '👮📌 Антикоррупция (блоки PDF верх стр.)'

    def __str__(self):
        return self.name


class Book_complaint(models.Model):
    """This Model for Book_complaint block on the main page"""

    name = models.CharField(max_length=100, default='Book Name')
    description = models.TextField(default='Book Description')

    class Meta:
        verbose_name = '📖 Книга жалоб и предложений'
        verbose_name_plural = '📖 Книга жалоб и предложений'

    def __str__(self):
        return self.name


class EducationalResource(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = HTMLField(verbose_name="Описание")
    pdf_file = models.FileField(upload_to='pdfs/', verbose_name="Прикрепить PDF")
    icon_class = models.CharField(max_length=100, default='fas fa-file-pdf')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🎓 Образовательные ресурсы (блоки PDF верх стр.)"
        verbose_name_plural = "🎓 Образовательные ресурсы (блоки PDF верх стр.)"
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
        verbose_name = "👨🏻‍⚕️ Доктора"
        verbose_name_plural = "👨🏻‍⚕️ Доктора"


class Services_title(models.Model):
    name = models.CharField(max_length=100, default='Service Name')
    description = models.TextField(default='Service Description')

    class Meta:
        verbose_name = '🛠️📌 Тайтл Услуги (блок с gif иконками, на стр.услуг и на главной стр.) 🇹 '
        verbose_name_plural = '🛠️📌 Тайтл Услуги (блок с gif иконками, на стр.услуг и на главной стр.)  🇹 '

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100, default='Service Name')
    description = models.TextField(default='Service Description')
    icon = models.ImageField(upload_to='service_icons/', null=True, blank=True)
    link = models.URLField()  # Поле для хранения ссылки

    class Meta:
        verbose_name = '🛠️📌 Услуги (gif иконки, на стр.услуг и на главной стр.)'
        verbose_name_plural = '🛠️📌 Услуги (gif иконки, на стр.услуг и на главной стр.)'

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
        verbose_name = '🏥ℹ️ Об Учреждении (блок с фото на гл.стр с описанием) 🇩'
        verbose_name_plural = '🏥ℹ️ Об Учреждении (блок с фото на гл.стр с описанием) 🇩'

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
        verbose_name = '🏥ℹ️ Об Учреждении Блок Исследования'
        verbose_name_plural = '🏥ℹ️ Об Учреждении Блок Исследования'

    def __str__(self):
        return self.name


class GeneralInfo(models.Model):
    title = models.CharField(max_length=100, default='Тайтл')
    description = HTMLField(max_length=200, default='Описание')

    class Meta:
        verbose_name = '💹📌 График Приёма Заголовок и описание  🇹 | 🇩'
        verbose_name_plural = '💹📌 График Приёма Заголовок и описание  🇹 | 🇩'

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
        verbose_name = '💹📌 Часы приема (таблица) 𝄜'
        verbose_name_plural = '💹📌 Часы приема (таблица) 𝄜'

    def __str__(self):
        return self.name


class Studies(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=500, default='Описание')
    indicators = models.TextField(default='Показатели')
    catering_workers = models.CharField(max_length=100, default='Работники торговли и общепита', blank=True, null=True)
    after_workers = models.CharField(max_length=100, default='Работники водоснабжения', blank=True, null=True)
    employees_school = models.CharField(max_length=100, default='Работники школ', blank=True, null=True)

    @property
    def catering_workers_display(self):
        return self.catering_workers or ''

    @property
    def after_workers_display(self):
        return self.after_workers or ''

    @property
    def employees_school_display(self):
        return self.employees_school or ''

    class Meta:
        verbose_name = '🧑‍🔬 Платные Услуги ФИЗ ЛИЦАМ - осмотр работающих таб1 𝄜'
        verbose_name_plural = '🧑‍🔬 Платные Услуги ФИЗ ЛИЦАМ - осмотр работающих (табл 1) 𝄜'

    def __str__(self):
        return self.name


class WaterQualitySafety(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=500, default='Описание')
    indicators = models.TextField(default='Показатели')
    mine_well = models.CharField(max_length=300, default='Шахтный колодец', blank=True, null=True)
    basic = models.CharField(max_length=300, default='Базовый', blank=True, null=True)
    standart = models.CharField(max_length=300, default='Стандарт', blank=True, null=True)
    standart_plus = models.CharField(max_length=300, default='Стандарт Плюс', blank=True, null=True)

    @property
    def mine_well_display(self):
        return self.mine_well or ''

    @property
    def basic_display(self):
        return self.basic or ''

    @property
    def standart_display(self):
        return self.standart or ''

    @property
    def standart_plus_display(self):
        return self.standart_plus or ''

    class Meta:
        verbose_name = '🧑‍🔬 Лабораторные исследования воды 🧪 на качество ⚛︎🧬🧫'
        verbose_name_plural = '🧑‍🔬 Лабораторные исследования воды 🧪 на качество и безопасность ⚛︎🧬🧫 (ФИЗ ЛИЦАМ табл 2) 𝄜'

    def __str__(self):
        return self.name


class LaboratoryFruitVegetable(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField(max_length=500, default='Описание')
    paket = models.TextField(default='Пакет исследований')
    cost = models.CharField(max_length=300, default='Цена', blank=True, null=True)

    @property
    def cost_display(self):
        return self.cost or ''

    class Meta:
        verbose_name = '🧑‍🔬 Лабораторные исследования плод/овощ 🥗 продукции'
        verbose_name_plural = '🧑‍🔬 Лабораторные исследования плодоовощной 🥗 продукции (ФИЗ ЛИЦАМ табл 3) 𝄜'

    def __str__(self):
        return self.name


class HotlineHours(models.Model):
    name = models.CharField(max_length=100, default='Фамилия Имя и Отчество')
    post = models.CharField(max_length=100, default='Должность')
    phone = models.CharField(max_length=100)
    reception_time = models.CharField(max_length=100, default='Время проведения прямой линии')
    date_hotline = models.CharField(max_length=100, default='Дата Проведения прям линии')

    class Meta:
        verbose_name = '☎️♨️ Прямая линия (таблица) 𝄜'
        verbose_name_plural = '☎️♨️ Прямая линия (таблица) 𝄜'

    def __str__(self):
        return self.name


class HotlineHours_Title(models.Model):
    name = models.CharField(max_length=100, default='Прямая Телефонная Линия')
    description = models.CharField(max_length=300, default='График проведения "прямой телефонной линии" в Государственном учреждении "Полоцкий зональный центр гигиены и эпидемиологии"')

    class Meta:
        verbose_name = '☎️♨️ Прямая линия тайтл и описание  🇹 | 🇩'
        verbose_name_plural = '☎️♨️ Прямая линия тайтл и описание  🇹 | 🇩'

    def __str__(self):
        return self.name


class HotlineHours_Title_desc(models.Model):
    name = models.CharField(max_length=300, default='Порядок проведения')
    description = models.CharField(max_length=3000, default='Описание проведения')

    class Meta:
        verbose_name = '☎️♨️ Прямая линия Порядок проведения (тайтл и описание)  🇹 | 🇩'
        verbose_name_plural = '☎️♨️ Прямая линия Порядок проведения (тайтл и описание)  🇹 | 🇩'

    def __str__(self):
        return self.name


class Electronic_appeals_Title_desc(models.Model):
    name = models.CharField(max_length=300, default='Порядок проведения')
    description = models.CharField(max_length=3000, default='Описание проведения')

    class Meta:
        verbose_name = '👨‍💻 Электронные Обращения (тайтл и описание)  🇹 | 🇩'
        verbose_name_plural = '👨‍💻 Электронные Обращения (тайтл и описание)  🇹 | 🇩'

    def __str__(self):
        return self.name


class Up_Organ_inf(models.Model):
    name = models.CharField(max_length=300, default='Телефон горячей линии')
    description = models.CharField(max_length=3000, default='Время работы')

    class Meta:
        verbose_name = '🗼🏙️ Вышестоящий Орган (телефон горячей линии низ стр.)'
        verbose_name_plural = '🗼🏙️ Вышестоящий Орган (телефон горячей линии низ стр.)'

    def __str__(self):
        return self.name


class Expertise(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    description = models.CharField(max_length=3000, default='Первое большое описание')
    description_two = models.CharField(max_length=3000, default='Второе описание')
    description_three = models.CharField(max_length=3000, default='Третье описание')

    class Meta:
        verbose_name = '🎖️🧪 Экспертиза'
        verbose_name_plural = '🎖️🧪 Экспертиза'

    def __str__(self):
        return self.name


class MaintenanceSchedule(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    description = models.CharField(max_length=3000, default='Большое описание')

    class Meta:
        verbose_name = '📅⏰ Порядок и Сроки Обжалования (тайтл и описание)  🇹 | 🇩'
        verbose_name_plural = '📅⏰ Порядок и Сроки Обжалования (тайтл и описание)  🇹 | 🇩'

    def __str__(self):
        return self.name


class Duties(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    description = models.CharField(max_length=7000, default='Большое описание')

    class Meta:
        verbose_name = '⚖️ Права и обязанности (тайтл и описание)  🇹 | 🇩'
        verbose_name_plural = '⚖️ Права и обязанности (тайтл и описание)  🇹 | 🇩'

    def __str__(self):
        return self.name


class Vacancies(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    vacancy = models.CharField(max_length=7000, default='Вакансия 1')
    vacancy_two = models.CharField(max_length=7000, default='Вакансия 2')
    vacancy_three = models.CharField(max_length=7000, default='Вакансия 3')

    class Meta:
        verbose_name = '👔🔍 Вакансии'
        verbose_name_plural = '👔🔍 Вакансии'

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
        verbose_name = '📧📢 Обращения главная стр.(тайтл и описание)  🇹 | 🇩'
        verbose_name_plural = '📧📢 Обращения главная стр.(тайтл и описание)  🇹 | 🇩'

    def __str__(self):
        return self.name


class NormativeDocuments(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    normative_desc = models.CharField(max_length=300, default='Описание под тайтл')

    class Meta:
        verbose_name = '📝🗂️ Нормативные документы (инфо ссылка на pravo.by)'
        verbose_name_plural = '📝🗂️ Нормативные документы (инфо ссылка на pravo.by)'

    def __str__(self):
        return self.name


class EconimicSouz(models.Model):
    name_main = models.CharField(max_length=300, default='Тайтл заглавный', blank=True)
    name = models.CharField(max_length=500, default='Тайтл')
    desc = models.CharField(max_length=1000, default='Описание под тайтл')
    pdf_file = models.FileField(upload_to='pdfs/', blank=True)
    link = models.URLField(blank=True)
    icon_class = models.CharField(max_length=100, default='fas fa-heartbeat')

    class Meta:
        verbose_name = '🤝🇺🇳 Еврозийский экономичекский союз'
        verbose_name_plural = '🤝🇺🇳 Еврозийский экономичекский союз'

    def __str__(self):
        return self.name


class Quarantine(models.Model):

    name_main = models.CharField(max_length=300, default='Тайтл заглавный', blank=True)
    name = models.CharField(max_length=500, default='Тайтл')
    name_single_main = models.CharField(max_length=1500, default='Тайтл для Новостной страницы')
    desc_single_main = models.TextField(default='Описание для Новостной страницы', blank=True)
    desc = models.TextField(default='Описание под тайтл', blank=True)
    desc_two = models.TextField(default='СКП', blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', blank=True)
    link = models.URLField(blank=True)
    icon_class = models.CharField(max_length=100, default='fas fa-heartbeat')

    class Meta:
        verbose_name = '🏥😷 Санитарно - Карантинные пункты (блоки )'
        verbose_name_plural = '🏥😷 Санитарно - Карантинные пункты (блоки)'

    def __str__(self):
        return self.name



class Organ_Title_desc(models.Model):
    name = models.CharField(max_length=300, default='Тайтл')
    description = models.CharField(max_length=3000, default='Описание')

    class Meta:
        verbose_name = '🧑‍⚖️ Вышестоящий орган (тайтл и описание)  🇹 | 🇩'
        verbose_name_plural = '🧑‍⚖️ Вышестоящий орган (тайтл и описание)  🇹 | 🇩'

    def __str__(self):
        return self.name


class Up_Organ(models.Model):
    name = models.CharField(max_length=100, default='Фамилия Имя и Отчество')
    post = models.CharField(max_length=100, default='Должность')
    phone = models.CharField(max_length=100)
    reception_time = models.CharField(max_length=200, default='Время Приема')

    class Meta:
        verbose_name = '🧑‍⚖️ Вышестоящий орган 𝄜 (таблица)'
        verbose_name_plural = '🧑‍⚖️ Вышестоящий орган 𝄜 (таблица)'

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=255, default='вопрос')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', blank=True, null=True)  # Added publication date field

    class Meta:
        verbose_name = '❓❓❓  Вопросы'
        verbose_name_plural = '❓❓❓ Вопросы'

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField(blank=True)

    class Meta:
        verbose_name = '💡🗣️ Ответ'
        verbose_name_plural = '💡🗣️ Ответы'

    def __str__(self):
        return self.answer_text


class Question_Ansver_title(models.Model):

    name = models.CharField(max_length=255, default='Заголовок')
    description = HTMLField(max_length=200, default='Описание')

    class Meta:
        verbose_name = '💡🗣️ Заголовок и Описание Ответов  🇹 | 🇩'
        verbose_name_plural = '💡🗣️ Заголовок и Описание Ответов  🇹 | 🇩'

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
        verbose_name = '🤸‍♂️🏀 Здоровый Образ Жизни'
        verbose_name_plural = '🤸‍♂️🏀 Здоровый Образ Жизни'

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
        verbose_name = '💉☣ Лабораторные услуги 🧪'
        verbose_name_plural = '💉☣ Лабораторные услуги 🧪'

    def __str__(self):
        return self.name


class Laboratories(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')
    photo = models.ImageField(upload_to='Laboratory/', null=True, blank=True)

    class Meta:
        verbose_name = '💉☣  Лабораторные услуги (2ая половина) 🧪'
        verbose_name_plural = '💉☣  Лабораторные услуги (2ая половина) 🧪'

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    description_three = models.TextField(default='Описание 3')

    class Meta:
        verbose_name = '📓✔️ АП Регистрация (перечень) 🇩'
        verbose_name_plural = '📓✔️ АП Регистрация (перечень) 🇩'

    def __str__(self):
        return self.name


class Relation(models.Model):
    """Model Relation"""
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = '👦✔️ АП в отношении граждан (тайтл и описание)  🇹 | 🇩'
        verbose_name_plural = '👦✔️ АП в отношении граждан (тайтл и описание)  🇹 | 🇩'

    def __str__(self):
        return self.name


class HumanResourcesDesc(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = '👦✔️ АП Кадровая Служба (название и описание)  🇹 | 🇩'
        verbose_name_plural = '👦✔️ АП Кадровая Служба (название и описание)  🇹 | 🇩'

    def __str__(self):
        return self.name


class HumanResources(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    number_ap = models.CharField(max_length=300, default='Номер административной процедуры')
    name_ap = models.CharField(max_length=300, default='Наименование административной процедуры')
    doc_ap = models.CharField(max_length=300, default='Документы и (или) сведения АП')
    size_ap = models.CharField(max_length=300, default='Размер Платы взымаемой при АП')

    class Meta:
        verbose_name = '👦✔️ АП Кадровая Служба (таблица) 𝄜'
        verbose_name_plural = '👦✔️ АП Кадровая Служба (таблица) 𝄜'

    def __str__(self):
        return self.number_ap


class AccountingDesc(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = '👦✔️ АП Бухгалтерия (тайтл и описание) 🇹 | 🇩'
        verbose_name_plural = '👦✔️ АП Бухгалтерия (тайтл и описание) 🇹 | 🇩'

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
        verbose_name = '👦✔️ АП Кадровая Служба (таблица Бухгалтерия) 𝄜'
        verbose_name_plural = '👦✔️ АП Кадровая Служба (таблица Бухгалтерия) 𝄜'

    def __str__(self):
        return self.number_ap


class UnionDesc(models.Model):
    name = models.CharField(max_length=150, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = '👦✔️ АП Профсоюз (тайтл и описание) 🇹 | 🇩'
        verbose_name_plural = '👦✔️ АП Профсоюз (тайтл и описание) 🇹 | 🇩'

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
        verbose_name = '👦✔️ АП Профсоюз 𝄜 (таблица)'
        verbose_name_plural = '👦✔️ АП Профсоюз 𝄜 (таблица)'

    def __str__(self):
        return self.number_ap


class ListingDecreeDesc(models.Model):
    name = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')

    class Meta:
        verbose_name = '👦✔️ АП Указ (в отношении граждан) 🇩'
        verbose_name_plural = '👦✔️ АП Указ (в отношении граждан) 🇩'

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
        verbose_name = '👦✔️ АП Указ (таблица) 𝄜'
        verbose_name_plural = '👦✔️ АП Указ (таблица) 𝄜'

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
        verbose_name = '🏥👩🏿‍⚕️ О центре Профсоюз таблицы с сотрудниками 𝄜'
        verbose_name_plural = '🏥👩🏿‍⚕️ О центре Профсоюз таблицы с сотрудниками 𝄜'

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
        verbose_name = '🏥👩🏿‍⚕️  О центре Профсоюз таб/сотрудник (таблица 2) 𝄜'
        verbose_name_plural = '🏥👩🏿‍⚕️  О центре Профсоюз таблицы с сотрудниками (таблица 2) 𝄜'

    def __str__(self):
        return self.name


class ProfsouzDesc(models.Model):
    name = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание - 1')
    description_two = models.TextField(default='Описание - 2')
    package = models.TextField(default='Состав')

    class Meta:
        verbose_name = '🏥👩🏿‍⚕️  О центре Профсоюз верхнее описание 🇩'
        verbose_name_plural = '🏥👩🏿‍⚕️  О центре Профсоюз верхнее описание 🇩'

    def __str__(self):
        return self.name


class ProfsouzDescOne(models.Model):
    name = models.CharField(max_length=350, default='Тайтл')
    name_main = models.CharField(max_length=350, default='Тайтл на страницу')
    description = models.TextField(default='Описание - 1')
    description_two = models.TextField(default='Описание - 2')
    package = models.TextField(default='Состав')

    class Meta:
        verbose_name = '🏥👩🏿‍⚕️ О центре Профсоюз описание таблицы 𝄜'
        verbose_name_plural = '🏥👩🏿‍⚕️ О центре Профсоюз таблицы 𝄜'

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
        verbose_name = '🏥👩🏿‍⚕️ О центре Профсоюз Иконки'
        verbose_name_plural = '🏥👩🏿‍⚕️ О центре Профсоюз Иконки'

    def __str__(self):
        return self.name


class Disinfection(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')

    class Meta:
        verbose_name = '🧼🚩 Дезинфекция главное 🇲 🇩'
        verbose_name_plural = '🧼🚩 Дезинфекция главное 🇲 🇩'

    def __str__(self):
        return self.name


class Deratization(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    photo = models.ImageField(upload_to='Deratization/', null=True, blank=True)

    class Meta:
        verbose_name = '🧼🚩 Дератизация описание 🇩'
        verbose_name_plural = '🧼🚩 Дератизация описание 🇩'

    def __str__(self):
        return self.name


class MonitoringPlan(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    photo = models.ImageField(upload_to='MonitoringPlan/', null=True, blank=True)

    class Meta:
        verbose_name = '📊 План Мониторинга 🇲 🇹 🇩'
        verbose_name_plural = '📊 План Мониторинга 🇲 🇹 🇩'

    def __str__(self):
        return self.name


class MonitoringPlanArkhive(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    photo = models.ImageField(upload_to='MonitoringPlanArkhive/', null=True, blank=True)

    class Meta:
        verbose_name = '📊 План Мониторинга Архив 🗄️🇹 🇩'
        verbose_name_plural = '📊 План Мониторинга Архив 🗄️🇹 🇩'

    def __str__(self):
        return self.name


class Disinsection(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    photo = models.ImageField(upload_to='Disinsection/', null=True, blank=True)

    class Meta:
        verbose_name = '🧼🚩 Дезинсекция описание 🇩'
        verbose_name_plural = '🧼🚩 Дезинсекция описание 🇩'

    def __str__(self):
        return self.name


class DisinfectionDesc(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    photo = models.ImageField(upload_to='Disinfection/', null=True, blank=True)

    class Meta:
        verbose_name = '🧼🚩 Дезинфекция описание 🇩'
        verbose_name_plural = '🧼🚩 Дезинфекция описание 🇩'

    def __str__(self):
        return self.name


class Inventory(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_main = models.CharField(max_length=350, default='Тайтл')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')

    class Meta:
        verbose_name = '👦✔️ АП перечень'
        verbose_name_plural = '👦✔️ АП перечень'

    def __str__(self):
        return self.name


class BlanksInventory(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_for_blanks = models.CharField(max_length=350, default='Тайтл для бланков(отображается один, первый)')
    blanks_all = models.TextField(default='Бланк для Имени например (Бланк для Юр лица)')
    up_file = models.FileField(upload_to='files/', default='Добавить файл')

    class Meta:
        verbose_name = '👦✔️ АП Бланки (перечень)'
        verbose_name_plural = '👦✔️ АП Бланки (перечень)'

    def __str__(self):
        return self.name


# class ControlNadzorTipical(models.Model):
#
#     name = models.CharField(max_length=350, default='Тайтл для админки')
#     name_typical = models.CharField(max_length=350, default='Тайтл')
#     description = models.TextField(default='Заголовок таблицы - 1')
#     description_two = models.TextField(default='Заголовок таблицы - 2')
#     description_three = models.TextField(default='Заголовок таблицы - 3')
#     number = models.CharField(max_length=350, default='Номер строки(ячейки в таблице)')
#     objects_control = models.TextField(default='Объекты контроля')
#     typical_violations = models.TextField(default='Типичные нарушения')
#     name_typical_violations = models.TextField(default='Наименования технических регламентов')
#     pub_date = models.DateTimeField(verbose_name='Дата Публикации', default=timezone.now)
#
#     class Meta:
#         verbose_name = 'Контрольно надзорная деятельность Типичные нарушения(таблица)'
#         verbose_name_plural = 'Контрольно надзорная деятельность Типичные нарушения(таблица)'
#
#     def __str__(self):
#         return self.name

class ControlNadzorTipical(models.Model):
    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_typical = models.CharField(max_length=350, default='Тайтл')
    description_for_all = models.TextField(default='Описание для всего')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', default=timezone.now)

    class Meta:
        verbose_name = '🕹️🧐 Конт/надзор деятельность Типичные нарушения(таблица) 𝄜'
        verbose_name_plural = '🕹️🧐 Контрольно надзорная деятельность Типичные нарушения(таблица) 𝄜'

    def __str__(self):
        return self.name


class ControlNadzorRow(models.Model):
    control_nadzor = models.ForeignKey(ControlNadzorTipical, related_name='rows', on_delete=models.CASCADE)
    number = models.CharField(max_length=350, default='Номер строки(ячейки в таблице)')
    objects_control = models.TextField(default='Объекты контроля')
    typical_violations = models.TextField(default='Типичные нарушения')
    name_typical_violations = models.TextField(default='Наименования технических регламентов')

    def __str__(self):
        return f"{self.control_nadzor.name} - {self.number}"



class CNadTipicalName(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_typical = models.CharField(max_length=350, default='Тайтл')

    class Meta:
        verbose_name = '🕹️🧐 Конт/надзор деятельность Типичные нарушения (Тайтл) 🇹'
        verbose_name_plural = '🕹️🧐 Контрольно надзорная деятельность Типичные нарушения(Тайтл) 🇹'

    def __str__(self):
        return self.name


class CustomProductsInf(models.Model):

    name = models.CharField(max_length=350, default='Тайтл (для админ)')
    name_typical = models.CharField(max_length=350, default='Тайтл')
    description_small = models.TextField(default='Не большое описание для гл.стр. Не стандартная Продукция')
    description = models.TextField(default='Описание')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', default=timezone.now)

    class Meta:
        verbose_name = '🕹️🧐 Конт/надзор деятельность Нестандартная продукция 𝄜'
        verbose_name_plural = '🕹️🧐 Контрольно надзорная деятельность Нестандартная продукция(таблица) 𝄜'

    def __str__(self):
        return self.name


class CustomProductsName(models.Model):

    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_typical = models.CharField(max_length=350, default='Тайтл')

    class Meta:
        verbose_name = '🕹️🧐 Конт/надзор деятельность Нестандартная продукция (Тайтл) 🇹'
        verbose_name_plural = '🕹️🧐 Контрольно надзорная деятельность Нестандартная продукция(Тайтл) 🇹'

    def __str__(self):
        return self.name


class EpidemialogyName(models.Model):

    name = models.CharField(max_length=350, default='Тайтл')

    class Meta:
        verbose_name = '☣️😷 Эпидемиалогия (Тайтл) 🇹'
        verbose_name_plural = '☣️😷 Эпидемиалогия (Тайтл) 🇹'

    def __str__(self):
        return self.name



class EpidemialogyTipical(models.Model):
    description_small = models.TextField(default='Описание для стр. Эпидемиалогия')
    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_epidem = models.CharField(max_length=350, default='Тайтл ля стр. Эпидемиалогия (h3)')
    description = models.TextField(default='Описание')
    photo = models.ImageField(upload_to='Epidemialogy/', null=True, blank=True)
    photo_two = models.ImageField(upload_to='Epidemialogy/', null=True, blank=True)
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', default=timezone.now)

    class Meta:
        verbose_name = '☣️😷 Эпидемиалогия (статьи) 📜'
        verbose_name_plural = '☣️😷 Эпидемиалогия (статьи) 📜'

    def __str__(self):
        return self.name


class ServicesLawyerName(models.Model):

    name = models.CharField(max_length=350, default='Тайтл')

    class Meta:
        verbose_name = '🪙💲 Пл услуги Юр лицам и ИП (Тайтл)'
        verbose_name_plural = '🪙💲 Пл услуги Юр лицам и ИП (Тайтл)'

    def __str__(self):
        return self.name



class ServicesLawyerTipical(models.Model):
    description_small = models.TextField(default='Описание для стр. Юр лиц и ИП')
    name = models.CharField(max_length=350, default='Тайтл для админки')
    name_lawyer = models.CharField(max_length=350, default='Тайтл ля стр. Юр лиц и ИП (h3)')
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Второе описание')
    photo = models.ImageField(upload_to='Lawyer/', null=True, blank=True)
    photo_two = models.ImageField(upload_to='Lawyer/', null=True, blank=True)
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', default=timezone.now)

    class Meta:
        verbose_name = '🪙💲 Пл услуги Юр лицам и ИП (статьи)'
        verbose_name_plural = '🪙💲 Пл услуги Юр лицам и ИП (статьи)'

    def __str__(self):
        return self.name


# class ImmunoprophylaxisInf(models.Model):
#
#     name = models.CharField(max_length=350, default='Тайтл')
#     name_page = models.CharField(max_length=350, default='Тайтл для страницы имунопрофилактика')
#     description = models.TextField(default='Описание')
#     pub_date = models.DateTimeField(verbose_name='Дата Публикации', default=timezone.now)
#
#     class Meta:
#         verbose_name = 'Иммунопрофилактика (название и краткое описание статьи)'
#         verbose_name_plural = 'Иммунопрофилактика (название и краткое описание статьи)'
#
#     def __str__(self):
#         return self.name


class ImmunoprophylaxisTipical(models.Model):

    name = models.CharField(max_length=350, default='Тайтл')
    name_block = models.CharField(max_length=350, default='Тайтл для гл.страницы имунопрофилактика')
    desc_main_page = models.CharField(max_length=400, default='Описание для гл.страницы имунопрофилактика (в блок)')
    description_single = models.TextField(default='Описание')
    photo = models.ImageField(upload_to='Immunoprofilactixs/', null=True, blank=True)
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', default=timezone.now)

    class Meta:
        verbose_name = '☣️😷 Иммунопрофилактика (статьи) 📜'
        verbose_name_plural = '☣️😷 Иммунопрофилактика (статьи) 📜'

    def __str__(self):
        return self.name


class InformationAnalytical(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    pdf_file = models.FileField(upload_to='pdfs/', verbose_name="Прикрепить PDF")
    icon_class = models.CharField(max_length=100, default='fas fa-file-pdf')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "📜📊 Информационно-аналитический бюллетень"
        verbose_name_plural = "📜📊 Информационно-аналитический бюллетень"
        ordering = ['-pub_date']


class HealthyTitle(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя Заголовка")
    description = models.TextField(default='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🏰🏋️ Зд/Гор и поселки (Верхний ТАЙТЛ и ОПИСАНИЕ) 🇹 | 🇩"
        verbose_name_plural = "🏰🏋️ Здоровые города и поселки (Верхний ТАЙТЛ и ОПИСАНИЕ) 🇹 | 🇩"


class Healthy(models.Model):
    name = models.CharField(max_length=300, verbose_name="Имя")
    name_taitle = models.CharField(max_length=100, verbose_name="Описание под тайтл")
    pdf_file = models.FileField(upload_to='pdfs/', verbose_name="Прикрепить PDF")
    icon_class = models.CharField(max_length=100, default='fas fa-file-pdf')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', blank=True, null=True)
    link = models.URLField(verbose_name="Ссылка", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🏰🏋️ Здоровые города и поселки (ФАЙЛЫ) 📁"
        verbose_name_plural = "🏰🏋️ Здоровые города и поселки (ФАЙЛЫ) 📁"
        ordering = ['-pub_date']


class Objectives(models.Model):
    name = models.CharField(max_length=300, verbose_name="Имя")
    description = models.TextField(default='Описание')
    icon_class = models.CharField(max_length=100, default='fas fa-file-pdf')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🎯📈 Цели устойчивого развития"
        verbose_name_plural = "🎯📈 Цели устойчивого развития"


class Ticks(models.Model):
    name = models.CharField(max_length=300, verbose_name="Имя")
    name_map = models.CharField(max_length=700, default="Имя для карт")
    description = models.TextField(default='Описание')
    description_two = models.TextField(default='Описание 2')
    google_map_embed_code = models.TextField(blank=True, null=True, verbose_name="Код вставки Google Карт")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "⚠️🪲 Внимание клещи"
        verbose_name_plural = "⚠️🪲 Внимание клещи"


class Ticks_files(models.Model):
    name = models.CharField(max_length=300, verbose_name="Имя")
    description = models.TextField(default='Описание')
    pdf_file = models.FileField(upload_to='pdfs/', verbose_name="Прикрепить PDF", null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "⚠️🪲 Внимание клещи (Блок с файлами) 📁"
        verbose_name_plural = "⚠️🪲 Внимание клещи (Блок с файлами) 📁"


class ContactInfoHad(models.Model):
    """Модель для хранения контактной информации и часов работы."""

    name = models.CharField(max_length=50, default='имя для админки')
    working_days = models.CharField(max_length=50, default="Пн - Пт, 8.00 - 17.00")
    lunch_time = models.CharField(max_length=50, default="Обед: 13.00 - 14.00")
    phone_number = models.CharField(max_length=50, default="Наш телефон: +80214493168")
    email_address = models.CharField(max_length=70, default="Наша почта: polotzk_hyg@vitebsk.by")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "📲🗺️ Контактная информация для Top Bar"
        verbose_name_plural = "📲🗺️ Контактная информация для Top Bar"


class EripPayment(models.Model):

    name = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    payment_methods = models.TextField(verbose_name="Схема проведения платежа")
    unp = models.TextField(verbose_name="УНП", blank=True)
    title_portal = models.TextField(verbose_name="ПОРТАЛ РЕЙТИНГОВОЙ ОЦЕНКИ", blank=True)
    payment_scheme_image1 = models.ImageField(upload_to='payment_schemes/', verbose_name="Схема проведения платежа 1")
    payment_scheme_image3 = models.ImageField(upload_to='payment_schemes/', verbose_name="Мальчик", blank=True)
    payment_scheme_image4 = models.ImageField(upload_to='payment_schemes/', verbose_name="Книжка", blank=True)
    payment_scheme_image5 = models.ImageField(upload_to='payment_schemes/', verbose_name="Стрелка", blank=True)
    payment_scheme_image6 = models.ImageField(upload_to='payment_schemes/', verbose_name="токен поратл", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🪙💲 ЕРИП данные"
        verbose_name_plural = "🪙💲 ЕРИП данные"


class PhotoDay(models.Model):

    name = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='photos_day/', verbose_name="для фото дня")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🖼️ Фото дня"
        verbose_name_plural = "🖼️ Фото дня"


class Contacts(models.Model):

    name = models.CharField(max_length=255, verbose_name="Заголовок")
    adres = models.TextField(verbose_name="Адрес")
    mail = models.TextField(verbose_name="Почта")
    phone = models.TextField(verbose_name="Телефон")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "📲🗺️ Контакты & данные"
        verbose_name_plural = "📲🗺️ Контакты & данные"


class CentreNews(models.Model):

    name = models.CharField(max_length=255, verbose_name="ИМЯ")
    pub_date = models.DateTimeField(verbose_name='Дата Публикации', blank=True, null=True)
    link = models.URLField(verbose_name="Ссылка", blank=True, null=True)
    desc = models.TextField(verbose_name="Описание")
    desc_hover = models.TextField(verbose_name="Описание при наведении")
    img = models.ImageField(verbose_name='photo', upload_to='CentreNews/')
    author = models.TextField(verbose_name="Автор")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "📰🌐 Блок с новостями(зелено-красный)"
        verbose_name_plural = "📰🌐 Блок с новостями(зелено-красный)"


class OurPartners (models.Model):

    name = models.CharField(max_length=200, verbose_name='Имя Слайдер партнеры')
    img = models.ImageField(verbose_name='Photo', upload_to='Slider-Partners/')
    link = models.URLField(verbose_name="Ссылка", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🧑‍🦲 Слайдер Партнеры"
        verbose_name_plural = "🧑‍🦲 Слайдер Партнеры"


class CitiesTitle(models.Model):
    """Модель для населенных пунктов"""
    name = models.CharField(max_length=350, default='Тайтл для блока города')

    class Meta:
        verbose_name = '🏰🏋️ Здоровые города и поселки (Тайтл для блока Посёлка) 🇹'
        verbose_name_plural = '🏰🏋️ Здоровые города и поселки (Тайтл для блока Посёлка) 🇹'

    def __str__(self):
        return self.name


class Cities(models.Model):
    """Модель для населенных пунктов"""
    name = models.CharField(max_length=350, default='Тайтл для Посёлка')
    name_city = models.CharField(max_length=350, default='Тайтл для Посёлка на странице посёлка')
    description = models.TextField(default='Описание для страницы Города/Посёлки')
    description_two = models.TextField(default='Описание для страницы Поселка')
    photo = models.ImageField(upload_to='Health_cities/', null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    file_desc = models.TextField(default='Description file')  # Поле для описания
    pdf_file = models.FileField(upload_to='city_documents/', blank=True, null=True)

    class Meta:
        verbose_name = '🏰🏋️ Здоровые города и поселки (Тайтл описание фото, добавить посёлок) 🇩'
        verbose_name_plural = '🏰🏋️ Здоровые города и поселки (Тайтл описание фото, добавить посёлок) 🇩'

    def __str__(self):
        return self.name


class CityDescription(models.Model):
    """Модель для описаний городов"""
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='descriptions')
    description_two = models.TextField(default='Описание при клике')
    description_three = models.TextField(default='Развернутое Описание')
    add_file = models.FileField(upload_to='pdfs/', verbose_name="Прикрепить PDF", blank=True)

    class Meta:
        verbose_name = '🏰🏋️ Здоровые города и поселки - Интерактивная Доска'
        verbose_name_plural = '🏰🏋️ Здоровые города и поселки - Интерактивная Доска'

    def __str__(self):
        return f"Описание {self.id}"


class NormativeDoc(models.Model):
    """This Model for Price Lists block on the main page"""

    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')
    link = models.URLField(blank=True)  # Поле для хранения ссылки
    icon_class = models.CharField(max_length=100, default='fas fa-file-invoice')
    add_file = models.FileField(upload_to='pdfs/', blank=True)

    class Meta:
        verbose_name = '📝🗂️ Нормативные документы (описание и файлы) 🇩'
        verbose_name_plural = '📝🗂️ Нормативные документы (описание и файлы) 🇩'

    def __str__(self):
        return self.name


class AboutHistory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Description')
    quantity = models.IntegerField(default=0)
    icon_class = models.CharField(max_length=50)

    class Meta:
        verbose_name = '🏥ℹ️ История - Описание (блоки на главной под фото) 🇩'
        verbose_name_plural = '🏥ℹ️ История - Описание (блоки на главной под фото) 🇩'

    def __str__(self):
        return self.name


class Structure(models.Model):
    """Structure page main model"""

    name = models.CharField(max_length=100, default='Name')
    description = models.TextField(default='Description')
    photo = models.ImageField(upload_to='Structure/', null=True, blank=True)

    class Meta:
        verbose_name = '🧬 Структура 👩🏻‍🔬⚗️🧪🥼'
        verbose_name_plural = '🧬 Структура 👩🏻‍🔬⚗️🧪🥼'

    def __str__(self):
        return self.name


class EnyPayment(models.Model):

    name = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    payment_where = models.TextField(verbose_name="Где сделать платёж")
    payment_methods = models.TextField(verbose_name="Схема проведения платежа")
    unp = models.TextField(verbose_name="УНП", blank=True)
    title_qr = models.TextField(verbose_name="Тайтл QR-кода Cashew", blank=True)
    qr_img = models.ImageField(upload_to='payment_schemes/', verbose_name="QR photo Токен", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🪙💲 ЕРИП платные услуги физ лицам"
        verbose_name_plural = "🪙💲 ЕРИП платные услуги физ лицам"


class Busel (models.Model):

    name = models.CharField(max_length=50, default='Busel')
    photo_busel = models.ImageField(upload_to='busel/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🐦🐥 Бусел (фото)"
        verbose_name_plural = "🐦🐥 Бусел (фото)"


class SliderMain(models.Model):
    """Главный слайдер (например, для страницы)"""
    name = models.CharField(max_length=300, default="Name Slider", null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "🎞️ 🖼️ Главный Слайдер"
        verbose_name_plural = "🎞️ 🖼️ Главный Слайдер"


class Slide(models.Model):
    """Отдельный слайд, принадлежащий слайдеру"""
    slider = models.ForeignKey(SliderMain, related_name='slides', on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to='slider/', null=True, blank=True)
    order = models.PositiveIntegerField(default=0, help_text='Порядок слайда')

    def __str__(self):
        return f"Слайд {self.order} для {self.slider.name}"

    class Meta:
        verbose_name = "🎞️ 🖼️ Слайд"
        verbose_name_plural = "🎞️ 🖼️ Слайды"
        ordering = ['order']
