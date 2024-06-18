from django.shortcuts import render
from news.models import Interactive, ModelNews, PreviewNews
from news.utils import get_weather
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
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    model_blog_main = ModelNews.objects.all().order_by('-pub_date')
    # Получаем данные о погоде
    weather = get_weather()
    interactiv = Interactive.objects.all()

    context = {
        'desc_services_title': desc_services_title,
        'main_services': main_services,
        'about_us': about_us,
        'innovations': innovations,
        'featured': featured,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'weather': weather,
        'model_blog_main': model_blog_main,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/index.html', context=context)


def chief_doctor(request):
    """Main Page Doctor Clinic"""

    return render(request, 'webapp/doctors/main_doctor.html')


def info_main(request):
    """Main Page Main Info of Clinic"""

    return render(request, 'webapp/informations/info_main.html')


# def news_main(request):
#     """Main News Clinic"""
#
#     features = Featured.objects.all()
#
#     context = {
#         'features': features,
#     }
#
#     return render(request, 'webapp/news/news_main.html', context=context)


def structure(request):
    """About us Structure template"""
    features = Featured.objects.all()
    questions = Question.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    context = {
        'features': features,
        'questions': questions,
        'title_desc_queans': title_desc_queans,
    }

    return render(request, 'webapp/about_us/structure.html', context=context)


def working_mode(request):
    """About us Structure template"""

    info_clocks = GeneralInfo.objects.all()
    clocks = ReceptionHours.objects.all()
    features = Featured.objects.all()

    context = {
        'features': features,
        'clocks': clocks,
        'info_clocks': info_clocks,
    }

    return render(request, 'webapp/about_us/working_mode.html', context=context)


def anti_corruption(request):
    """Anti-corruption template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/about_us/anti_corruption.html', context=context)


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
    title_desc = HotlineHours_Title.objects.all()
    title_desc_two = Electronic_appeals_Title_desc.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    interactiv = Interactive.objects.all()

    context = {
        'features': features,
        'title_desc': title_desc,
        'title_desc_two': title_desc_two,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/appeals/electronic_appeals.html', context=context)


def hotline(request):
    """Appeals - hotline template"""
    features = Featured.objects.all()
    clocks = HotlineHours.objects.all()
    title_desc = HotlineHours_Title.objects.all()
    title_desc_two = HotlineHours_Title_desc.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    context = {
        'features': features,
        'clocks': clocks,
        'title_desc': title_desc,
        'title_desc_two': title_desc_two,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
    }

    return render(request, 'webapp/appeals/hotline.html', context=context)


def book_of_comments(request):
    """Appeals - book_of_comments template"""
    features = Featured.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    book_info = Book_complaint.objects.all()
    interactiv = Interactive.objects.all()


    context = {
        'features': features,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
        'book_info': book_info,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/appeals/book_of_comments.html', context=context)


def higher_authority(request):
    """Appeals - higher_authority template"""
    interactiv = Interactive.objects.all()
    title_organ = Organ_Title_desc.objects.all()
    table =Up_Organ.objects.all()
    title_desc_inf = Up_Organ_inf.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    context = {
        'interactiv': interactiv,
        'title_organ': title_organ,
        'table': table,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
        'title_desc_inf': title_desc_inf,
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
    main_services = Services.objects.all()
    features = Featured.objects.all()
    questions = Question.objects.all()
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    context = {
        'features': features,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'main_services': main_services,
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


def custom_products(request):
    """Activity - custom_products template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/custom_products.html', context=context)


def healthy_cities_towns(request):
    """Activity - healthy_cities_towns template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/healthy_cities_towns.html', context=context)


def eurasian_economic_union(request):
    """Activity - eurasian_economic_union template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/eurasian_economic_union.html', context=context)


def sanitary_quarantine_points(request):
    """Activity - sanitary_quarantine_points template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/sanitary_quarantine_points.html', context=context)


def epidemiology(request):
    """Activity - epidemiology template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/epidemiology.html', context=context)


def immunoprophylaxis(request):
    """Activity - immunoprophylaxis template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/immunoprophylaxis.html', context=context)


def sustainable_development_goals(request):
    """Activity - sustainable_development_goals template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/sustainable_development_goals.html', context=context)


def analytical_newsletter(request):
    """Activity - analytical_newsletter template"""
    features = Featured.objects.all()

    context = {
        'features': features,
    }

    return render(request, 'webapp/activity/analytical_newsletter.html', context=context)


def healthy_lifestyle(request):
    """Healthy_lifestyle - healthy_lifestyle template"""
    features = Featured.objects.all()
    preview = PreviewNews.objects.filter(is_health_news=True)
    interactiv = Interactive.objects.all()
    model_blog_main = ModelNews.objects.filter(is_health_news=True).order_by('-pub_date')
    zoj = Zoj.objects.all()

    context = {
        'features': features,
        'preview': preview,
        'interactiv': interactiv,
        'model_blog_main': model_blog_main,
        'zoj': zoj,
    }

    return render(request, 'webapp/healthy_lifestyle/healthy_lifestyle.html', context=context)


def preventive_measures(request):
    """Healthy_lifestyle - preventive_measures template"""
    features = Featured.objects.all()
    model_blog_main = ModelNews.objects.filter(is_main_measures=True).order_by('-pub_date')
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()

    context = {
        'features': features,
        'model_blog_main': model_blog_main,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
        'ansvers': ansvers,
    }

    return render(request, 'webapp/healthy_lifestyle/preventive_measures.html', context=context)


def health_days(request):
    """Healthy_lifestyle - health_days template"""
    features = Featured.objects.all()
    interactiv = Interactive.objects.all()
    preview = PreviewNews.objects.all()
    model_blog_main = ModelNews.objects.filter(is_main_days_health=True).order_by('-pub_date')
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()

    context = {
        'features': features,
        'interactiv': interactiv,
        'preview': preview,
        'model_blog_main': model_blog_main,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
        'ansvers': ansvers,
    }

    return render(request, 'webapp/healthy_lifestyle/health_days.html', context=context)


def educational_resources(request):
    """Healthy_lifestyle - educational_resources template"""
    features = Featured.objects.all()
    interactiv = Interactive.objects.all()
    see_pdf = EducationalResource.objects.all().order_by('-pub_date')
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()

    context = {
        'features': features,
        'interactiv': interactiv,
        'see_pdf': see_pdf,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
        'ansvers': ansvers,
    }

    return render(request, 'webapp/healthy_lifestyle/educational_resources.html', context=context)


def contacts(request):
    """Contacts template"""
    features = Featured.objects.all()
    interactiv = Interactive.objects.all()

    context = {
        'features': features,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/contacts.html', context=context)
