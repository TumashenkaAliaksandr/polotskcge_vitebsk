from django.contrib.sitemaps import Sitemap
from ..models import ModelNews

class PostSitemap(Sitemap):
    changefreq = 'weekly'  # Частота изменения страницы
    priority = 0.8  # Важность страницы

    def items(self):
        return ModelNews.objects.all().order_by('title', 'description_small')

    def lastmod(self, obj):
        return obj.pub_date  # Возвращаем поле pub_date как объект datetime

    def location(self, obj):
        return f'/cge_news/{obj.pk}/'  # URL для новости

    def get_urls(self, site=None, **kwargs):
        urls = super().get_urls(site=site, **kwargs)
        for item in self.items():
            urls.append({
                'location': self.location(item),  # URL для новости
                'lastmod': item.pub_date.strftime('%Y-%m-%d'),  # Форматируем дату
                'changefreq': self.changefreq,
                'priority': self.priority,
                'title': item.title,
                'description': item.description_small,
            })
        return urls
