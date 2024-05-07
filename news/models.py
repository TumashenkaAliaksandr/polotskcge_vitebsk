from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


class ModelNews(models.Model):
    """Main model News"""

    title = models.CharField(max_length=200, verbose_name='Название')
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главная модель Новости'
        verbose_name_plural = 'Главная модель Новости'

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
    link = models.URLField()  # Поле для хранения ссылки

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Превью новостей'
        verbose_name_plural = 'Превью новостей'


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название видео')
    video_file = models.FileField(upload_to='videos/', verbose_name='Видео файл')
    description = RichTextField(verbose_name='Краткое описание')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    author = models.CharField(max_length=100, verbose_name='Автор')
    category = models.CharField(max_length=100, verbose_name='Название рубрики')
    is_featured = models.BooleanField(default=False, verbose_name='На главный экран')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео Новости'
        verbose_name_plural = 'Видео Новости'

