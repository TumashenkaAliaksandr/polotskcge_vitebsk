from news.models import *
from django.shortcuts import render, get_object_or_404

from webapp.models import CentreNews, PhotoDay
from .utils import get_weather
from django.core.paginator import Paginator


def cge_news(request):
    """these are views for Blog News list"""

    model_blog_main = ModelNews.objects.all().order_by('-pub_date')

    # Получаем все новости, отсортированные по дате
    all_news = ModelNews.objects.all().order_by('-pub_date')

    # Получаем популярные и природные новости
    popular_news = all_news.filter(is_popular=True)[:4]
    nature_news = all_news.filter(is_nature_news=True)[:4]

    # Получаем интерактивные элементы, превью новостей и видео
    interactiv = Interactive.objects.all()
    preview = PreviewNews.objects.all()
    model_video = Video.objects.all().order_by('-timestamp')

    # Пагинация: разбиваем новости на страницы по 10 новостей на страницу
    paginator = Paginator(all_news, 3)  # По 10 новостей на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    centre_news = CentreNews.objects.all().order_by('-pub_date')
    # Получаем данные о погоде
    weather = get_weather()
    photo_day = PhotoDay.objects.all()

    context = {
        'model_blog_main': model_blog_main,
        'interactiv': interactiv,
        'preview': preview,
        'page_obj': page_obj,  # Страница новостей для отображения
        'model_video': model_video,
        'weather': weather,
        'popular_news': popular_news,
        'nature_news': nature_news,
        'centre_news': centre_news,
        'photo_day': photo_day,
    }

    return render(request, 'breaking.html', context=context)


def one_news(request, pk, slug):
    """these are views for Blog News list"""
    news = get_object_or_404(ModelNews, pk=pk, slug=slug)

    context = {
        'news': news,
    }
    return render(request, 'breaking.html', context=context)


def NewsDetailView(request, slug):
    """Views for News details"""
    news = get_object_or_404(ModelNews, slug=slug)
    news_main = ModelNews.objects.all().order_by('-pub_date')
    interactiv = Interactive.objects.all()
    centre_news = CentreNews.objects.all().order_by('-pub_date')
    photo_day = PhotoDay.objects.all()

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'news': news,
        'news_main': news_main,
        'interactiv': interactiv,
        'weather': weather,  # Передаем данные о погоде в контекст
        'centre_news': centre_news,
        'photo_day': photo_day,
    }

    return render(request, 'single.html', context=context)
