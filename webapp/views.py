from django.shortcuts import render
from webapp.models import *


def base_main(request):
    """main base template"""

    logo_main = Logo.objects.all()

    context = {
        'logo_main': logo_main,
    }

    return render(request, 'main/base.html', context=context)


def index(request):
    """Main, center"""

    main_services = Services.objects.all()
    desc_services_title = Services_title.objects.all()
    about_us = AboutUs.objects.all()
    innovations = Researches.objects.all()
    featured = Featured.objects.all()

    context = {
        'desc_services_title': desc_services_title,
        'main_services': main_services,
        'about_us': about_us,
        'innovations': innovations,
        'featured': featured,
    }

    return render(request, 'webapp/index.html', context=context)


def chief_doctor(request):
    """Main Page Doctor Clinic"""

    return render(request, 'webapp/doctors/main_doctor.html')


def info_main(request):
    """Main Page Main Info of Clinic"""

    return render(request, 'webapp/informations/info_main.html')

def news_main(request):
    """Main News Clinic"""

    return render(request, 'webapp/news/news_main.html')


def structure(request):
    """About us Structure template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/about_us/structure.html', context=context)


def working_mode(request):
    """About us Structure template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/about_us/structure.html', context=context)


def anti_corruption(request):
    """Anti-corruption template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/about_us/structure.html', context=context)


def ideological_work(request):
    """Ideological_work template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/about_us/ideological_work.html', context=context)


def charter(request):
    """Charter template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/about_us/charter.html', context=context)


def trade_union(request):
    """Trade union template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/about_us/trade_union.html', context=context)


def vacancies(request):
    """Trade union template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/about_us/vacancies.html', context=context)


def appeals(request):
    """Appeals template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/appeals/main_appeals.html', context=context)


def normative_documents(request):
    """Appeals - normative_documents template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/appeals/normative_documents.html', context=context)


def electronic_appeals(request):
    """Appeals - electronic_appeals template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/appeals/electronic_appeals.html', context=context)


def hotline(request):
    """Appeals - hotline template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/appeals/hotline.html', context=context)


def book_of_comments(request):
    """Appeals - book_of_comments template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/appeals/book_of_comments.html', context=context)


def higher_authority(request):
    """Appeals - higher_authority template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/appeals/higher_authority.html', context=context)
