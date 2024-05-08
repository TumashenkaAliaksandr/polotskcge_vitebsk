from news.models import *
from django.shortcuts import render
from .utils import get_weather
from django.core.paginator import Paginator



def news(request):
    """these are views for Blog News list"""
    model_blog_main = ModelNews.objects.all().order_by('-pub_date')
    all_news = ModelNews.objects.all()
    popular_news = all_news.filter(is_popular=True)[:4]
    nature_news = all_news.filter(is_nature_news=True)[:4]
    interactiv = Interactive.objects.all()
    preview = PreviewNews.objects.all()
    all_news = ModelNews.objects.all().order_by('-pub_date')
    paginator = Paginator(all_news, 10)  # По 10 новостей на страницу
    model_video = Video.objects.all().order_by('-timestamp')
    # Получаем данные о погоде
    weather = get_weather()

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'model_blog_main': model_blog_main,
        'interactiv': interactiv,
        'preview': preview,
        'page_obj': page_obj,
        'model_video': model_video,
        'weather': weather,
        'popular_news': popular_news,
        'nature_news': nature_news,
    }
    return render(request, 'breaking.html', context=context)


def one_news(request, pk):
    """these are views for Blog News list"""
    news = ModelNews.objects.filter(pk=pk)

    context = {
        'news': news,
    }
    return render(request, 'breaking.html', context=context)


def NewsDetailView(request, pk):
    """Views for News details"""
    news = ModelNews.objects.filter(pk=pk)
    news_main = ModelNews.objects.all().order_by('-pub_date')
    interactiv = Interactive.objects.all()

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'news': news,
        'news_main': news_main,
        'interactiv': interactiv,
        'weather': weather,  # Передаем данные о погоде в контекст
    }
    return render(request, 'single.html', context=context)
