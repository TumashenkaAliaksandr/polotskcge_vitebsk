from django.db import models
from django.conf import settings


class ModelNews(models.Model):
    """Main model News"""

    title = models.CharField(max_length=200, verbose_name='Name')
    description_small = models.TextField(max_length=500, default='', verbose_name='Description_small')
    description = models.TextField(verbose_name='Description', default='')
    description_company = models.TextField(verbose_name='Description_company', default='Описание для нижнего блока')
    location = models.CharField(max_length=200, verbose_name='Location', default='')
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Photo')
    logo_photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Logo Photo')
    pub_date = models.DateTimeField(verbose_name='Publication Date')  # Added publication date field
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author', related_name='news', null=True, blank=True)
    author_photo = models.ImageField(upload_to='author_photos/', null=True, blank=True, verbose_name='Author Photo')
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                       verbose_name='Comment Author', related_name='comments', null=True, blank=True)
    comment = models.TextField(verbose_name='Comment', default='Your default comment here')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Превью новостей'
        verbose_name_plural = 'Превью новостей'
