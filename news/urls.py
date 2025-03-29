from django.contrib.sitemaps.views import sitemap
from django.urls import path

from news.templates.sitemap import PostSitemap
from news.views import *

app_name = 'news'

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('cge_news/', cge_news, name='cge_news'),
    path('news/<int:pk>/<slug:slug>/', NewsDetailView, name='single'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
