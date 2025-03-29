from django.db import models
from django.conf import settings
from django.urls import reverse
from tinymce.models import HTMLField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from webapp.models import Cities


class ModelNews(models.Model):
    """Main model News"""

    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL-адрес', default="default-slug")
    description_small = models.TextField(max_length=500, default='', verbose_name='Не большое описание')
    description = models.TextField(verbose_name='Описание', default='Описание')
    description_company = models.TextField(verbose_name='Описание для нижнего блока', default='Описание для нижнего блока')
    location = models.CharField(max_length=200, verbose_name='Место где (локация)', default='')
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Фото')
    logo_photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Фото(маленькое)')
    pub_date = models.DateTimeField(verbose_name='Дата Публикации')  # Added publication date field
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', related_name='news', null=True, blank=True)
    author_photo = models.ImageField(upload_to='author_photos/', null=True, blank=True, verbose_name='Фото автора')
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                       verbose_name='Комментарий автора', related_name='comments', null=True, blank=True)
    comment = models.TextField(verbose_name='Примечание', default='Примечание')
    # Добавлены поля для "Популярные" и "Новости о природе"
    is_popular = models.BooleanField(verbose_name='Популярные', default=False, blank=True)
    is_city = models.BooleanField(verbose_name='Города/Посёлки', default=False, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='news', null=True, blank=True)  # Связь с городом
    is_nature_news = models.BooleanField(verbose_name='Новости о природе', default=False, blank=True)
    is_health_news = models.BooleanField(verbose_name='Новости о здоровье', default=False, blank=True)
    is_sport_news = models.BooleanField(verbose_name='Новости спорта', default=False, blank=True)
    is_economic_news = models.BooleanField(verbose_name='Новости экономики', default=False, blank=True)
    is_main_news = models.BooleanField(verbose_name='Важное', default=False, blank=True)
    is_main_measures = models.BooleanField(verbose_name='Профилактитческие мероприятия', default=False, blank=True)
    is_main_days_health = models.BooleanField(verbose_name='Единые дни здоровья', default=False, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:single', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })  # Замените 'news_detail' на имя вашего URL-шаблона

    class Meta:
        verbose_name = 'Главная модель Новости'
        verbose_name_plural = 'Главная модель Новости'

# Сигнал для автоматического формирования слага
# Стало (используем title)
@receiver(pre_save, sender=ModelNews)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        base_slug = slugify(instance.title)
        unique_slug = base_slug
        num = 1
        while ModelNews.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{num}"
            num += 1
        instance.slug = unique_slug


class Interactive(models.Model):
    """Model for interactiv menu News"""

    name = models.CharField(max_length=200, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', default='')
    description_two = models.TextField(verbose_name='Второе Описание', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Интерактитвная новость'
        verbose_name_plural = 'Интерактитвная новость'


class PreviewNews(models.Model):
    """Model for main news page Preview Model News"""

    title = models.CharField(max_length=200, verbose_name='Название превью')
    description = models.TextField(verbose_name='Описание', default='')
    photo = models.ImageField(upload_to='news_preview_photos/', null=True, blank=True,
                              verbose_name='Фотографии Превью Новостей')
    # Добавлены поля для "Популярные" и "Новости о природе"
    is_popular = models.BooleanField(verbose_name='Популярные', default=False, blank=True)
    is_nature_news = models.BooleanField(verbose_name='Новости о природе', default=False, blank=True)
    is_health_news = models.BooleanField(verbose_name='Новости о здоровье', default=False, blank=True)
    is_sport_news = models.BooleanField(verbose_name='Новости спорта', default=False, blank=True)
    is_economic_news = models.BooleanField(verbose_name='Новости экономики', default=False, blank=True)
    is_main_news = models.BooleanField(verbose_name='Важное', default=False, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Превью новостей'
        verbose_name_plural = 'Превью новостей'


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название видео')
    video_file = models.FileField(upload_to='videos/', verbose_name='Видео файл')
    description = HTMLField(verbose_name='Краткое описание')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    author = models.CharField(max_length=100, verbose_name='Автор')
    category = models.CharField(max_length=100, verbose_name='Название рубрики')
    is_featured = models.BooleanField(default=False, verbose_name='На главный экран')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео Новости'
        verbose_name_plural = 'Видео Новости'

