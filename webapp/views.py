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

    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/news/news_main.html', context=context)


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


def normative_documents_ap(request):
    """AP - normative_documents_ap template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/ap/normative_documents_ap.html', context=context)


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


def ap(request):
    """AP template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/ap/ap.html', context=context)


def expertise(request):
    """AP - expertise template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/ap/expertise.html', context=context)


def registrations(request):
    """AP - registrations template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/ap/registration.html', context=context)


def relation_to_citizens(request):
    """AP - relation_to_citizens template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/ap/relation_to_citizens.html', context=context)


def rights_duties(request):
    """AP - rights_duties template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/ap/rights_duties.html', context=context)


def maintenance_schedule(request):
    """AP - maintenance_schedule template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/ap/maintenance_schedule.html', context=context)


def services(request):
    """Services - services template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/services/services.html', context=context)


def paid_services(request):
    """Services - paid_services template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/services/paid_services.html', context=context)


def hygienic_services(request):
    """Services - hygienic template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/services/hygienic.html', context=context)



def laboratory_services(request):
    """Services - laboratory_services template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/services/laboratory_services.html', context=context)


def hygiene_education(request):
    """Services - hygiene_education template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/services/hygiene_education.html', context=context)


def disinfection_disinsection_deratization(request):
    """Services - disinfection_disinsection_deratization template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/services/disinfection_disinsection_deratization.html', context=context)


def npa(request):
    """NPA template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/npa.html', context=context)


def activity(request):
    """Activity template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/activity.html', context=context)


def supervisory_activities(request):
    """Activity - supervisory_activities template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/supervisory_activities.html', context=context)


def inspection_plan(request):
    """Activity - inspection_plan template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/inspection_plan.html', context=context)


def monitoring_plan(request):
    """Activity - monitoring_plan template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/monitoring_plan.html', context=context)


def typical_violations(request):
    """Activity - typical_violations template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/typical_violations.html', context=context)


def check_lists(request):
    """Activity - check_lists template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/check_lists.html', context=context)