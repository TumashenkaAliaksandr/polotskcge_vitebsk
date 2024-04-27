from news.models import *
from django.shortcuts import render



def news(request):
    """these are views for Blog News list"""
    model_blog_main = ModelNews.objects.all()

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
    news_blog_main = ModelNews.objects.all()

    context = {
        'news': news,
        'news_blog_main': news_blog_main,
    }
    return render(request, 'single.html', context=context)
