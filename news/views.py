from news.models import *
from django.shortcuts import render
from .utils import get_weather



def news(request):
    """these are views for Blog News list"""
    model_blog_main = ModelNews.objects.all().order_by('-pub_date')
    interactiv = Interactive.objects.all()
    preview = PreviewNews.objects.all()

    context = locals()
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
