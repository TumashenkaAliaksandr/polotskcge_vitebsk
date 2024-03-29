from django.shortcuts import render

from webapp.models import *


def index(request):
    """Main, center"""

    main_services = Services.objects.all()
    desc_services_title = Services_title.objects.all()
    about_us = AboutUs.objects.all()

    context = {
        'desc_services_title': desc_services_title,
        'main_services': main_services,
        'about_us': about_us,
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
