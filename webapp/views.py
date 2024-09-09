from django.shortcuts import render

from news.models import Interactive, ModelNews, PreviewNews
from news.utils import get_weather
from webapp.models import *


def base_main(request):
    """main base template"""
    logo_main = Logo.objects.all()
    info_contact = ContactInfoHad.objects.first()

    context = {
        'logo_main': logo_main,
        'info_contact': info_contact,
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
    sliders = OurPartners.objects.all()

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
        'sliders': sliders,
    }

    return render(request, 'webapp/index.html', context=context)


def chief_doctor(request):
    """Main Page Doctor Clinic"""

    return render(request, 'webapp/doctors/main_doctor.html')


def info_main(request):
    """Main Page Main Info of Clinic"""

    return render(request, 'webapp/informations/info_main.html')


def news_block(request):
    """Main Page News Info of Clinic"""
    model_blog_main = ModelNews.objects.all().order_by('-pub_date')

    context = {
        'model_blog_main': model_blog_main,
    }

    return render(request, 'main/mobile_news_index.html', context=context)


def structure(request):
    """About us Structure template"""
    features = Featured.objects.all()
    questions = Question.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    interactiv = Interactive.objects.all()

    context = {
        'features': features,
        'questions': questions,
        'title_desc_queans': title_desc_queans,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/about_us/structure.html', context=context)


def working_mode(request):
    """About us Structure template"""

    info_clocks = GeneralInfo.objects.all()
    clocks = ReceptionHours.objects.all()

    context = {
        'clocks': clocks,
        'info_clocks': info_clocks,
    }

    return render(request, 'webapp/about_us/working_mode.html', context=context)


def anti_corruption(request):
    """Anti-corruption template"""
    anticorr_title = AnticorrTitle.objects.all()
    corruptions = Anticorr.objects.all()
    interactiv = Interactive.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')

    context = {
        'anticorr_title': anticorr_title,
        'corruptions': corruptions,
        'interactiv': interactiv,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
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
    interactiv = Interactive.objects.all()
    profsouz_inf = ProfsouzDesc.objects.all()
    profsouz_inf_two = ProfsouzDescOne.objects.all()
    profsouz_infall = Profsouz.objects.all()
    profsouz_icons = ProfsouzIcons.objects.all()
    profsouz_inf_three = ProfsouzTwo.objects.all()


    context = {
        'interactiv': interactiv,
        'profsouz_inf': profsouz_inf,
        'profsouz_infall': profsouz_infall,
        'profsouz_icons': profsouz_icons,
        'profsouz_inf_two': profsouz_inf_two,
        'profsouz_inf_three': profsouz_inf_three,
    }

    return render(request, 'webapp/about_us/trade_union.html', context=context)


def vacancies(request):
    """Trade union template"""
    interactiv = Interactive.objects.all()
    vacancies_inf = Vacancies.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')

    context = {
        'interactiv': interactiv,
        'vacancies_inf': vacancies_inf,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
    }

    return render(request, 'webapp/about_us/vacancies.html', context=context)


def appeals(request):
    """Appeals template"""
    main_appeals_inf = MainAppeals.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    interactiv = Interactive.objects.all()

    context = {
        'main_appeals_inf': main_appeals_inf,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/appeals/main_appeals.html', context=context)


def normative_documents(request):
    """Appeals - normative_documents template"""
    main_normative_doc_inf = NormativeDocuments.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    interactiv = Interactive.objects.all()

    context = {
        'main_normative_doc_inf': main_normative_doc_inf,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/appeals/normative_documents.html', context=context)


def normative_documents_ap(request):
    """AP - normative_documents_ap template"""
    interactiv = Interactive.objects.all()
    centre_news = CentreNews.objects.all().order_by('-pub_date')

    context = {
        'interactiv': interactiv,
        'centre_news': centre_news,
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
    centre_news = CentreNews.objects.all().order_by('-pub_date')
    model_blog_main = ModelNews.objects.filter(is_main_days_health=True).order_by('-pub_date')

    context = {
        'features': features,
        'clocks': clocks,
        'title_desc': title_desc,
        'title_desc_two': title_desc_two,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'centre_news': centre_news,
        'model_blog_main': model_blog_main,
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
    inventory_info = Inventory.objects.all()
    blanks = BlanksInventory.objects.all()

    context = {
        'inventory_info': inventory_info,
        'blanks': blanks,
    }

    return render(request, 'webapp/ap/ap.html', context=context)


def expertise(request):
    """AP - expertise template"""
    interactiv = Interactive.objects.all()
    expertise_inf = Expertise.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')

    context = {
        'interactiv': interactiv,
        'expertise_inf': expertise_inf,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
    }

    return render(request, 'webapp/ap/expertise.html', context=context)


def registrations(request):
    """AP - registrations template"""
    reg_inf = Registration.objects.all()
    interactiv = Interactive.objects.all()

    context = {
        'reg_inf': reg_inf,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/ap/registration.html', context=context)


def relation_to_citizens(request):
    """AP - relation_to_citizens template"""
    interactiv = Interactive.objects.all()
    rel_inf = Relation.objects.all()
    table_inf = HumanResources.objects.all()
    hr_inf = HumanResourcesDesc.objects.all()
    accounting_inf = Accounting.objects.all()
    accounting_desc = AccountingDesc.objects.all()
    union_desc = UnionDesc.objects.all()
    union_inf = Union.objects.all()
    degree_desc = ListingDecreeDesc.objects.all()
    degree_inf = ListingDecree.objects.all()

    context = {
        'rel_inf': rel_inf,
        'hr_inf': hr_inf,
        'table_inf': table_inf,
        'accounting_inf': accounting_inf,
        'accounting_desc': accounting_desc,
        'union_desc': union_desc,
        'union_inf': union_inf,
        'degree_desc': degree_desc,
        'degree_inf': degree_inf,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/ap/relation_to_citizens.html', context=context)


def rights_duties(request):
    """AP - rights_duties template"""
    interactiv = Interactive.objects.all()
    duties_inf = Duties.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')

    context = {
        'interactiv': interactiv,
        'duties_inf': duties_inf,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
    }

    return render(request, 'webapp/ap/rights_duties.html', context=context)


def maintenance_schedule(request):
    """AP - maintenance_schedule template"""
    interactiv = Interactive.objects.all()
    maintenanceSch_inf = MaintenanceSchedule.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')

    context = {
        'interactiv': interactiv,
        'maintenanceSch_inf': maintenanceSch_inf,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
    }

    return render(request, 'webapp/ap/maintenance_schedule.html', context=context)


def services(request):
    """Services - services template"""

    desc_services_title = Services_title.objects.all()
    main_services = Services.objects.all()
    features = Featured.objects.all()
    questions = Question.objects.all()
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    interactiv = Interactive.objects.all()

    context = {
        'features': features,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'desc_services_title': desc_services_title,
        'main_services': main_services,
        'interactiv': interactiv,
    }

    return render(request, 'webapp/services/services.html', context=context)


def paid_services(request):
    """Services - paid_services template"""
    info_clocks = GeneralInfo.objects.all()
    studi = Studies.objects.all()
    wqs = WaterQualitySafety.objects.all()
    lfv = LaboratoryFruitVegetable.objects.all()
    price_lists_fiz = PriceListsFiz.objects.all()

    context = {
        'studi': studi,
        'wqs': wqs,
        'lfv': lfv,
        'info_clocks': info_clocks,
        'price_lists_fiz': price_lists_fiz,
    }

    return render(request, 'webapp/services/paid_services.html', context=context)


def paid_services_lawyer(request):
    """Services - hygienic template"""
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    lawyer_title = ServicesLawyerName.objects.all()

    all_typical_news = ServicesLawyerTipical.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'interactiv': interactiv,
        'lawyer_title': lawyer_title,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
    }

    return render(request, 'webapp/services/paid_services_lawyer.html', context=context)


def paid_services_lawyer_single(request, pk):
    """Activity - epidemiology template"""
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    typical_inf = ServicesLawyerTipical.objects.filter(pk=pk)
    epidem_title = EpidemialogyName.objects.all()


    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'interactiv': interactiv,
        'epidem_title': epidem_title,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'typical_inf': typical_inf,
    }

    return render(request, 'webapp/services/paid_services_lawyer_single.html', context=context)


def laboratory_services(request):
    """Services - laboratory_services template"""
    main_normative_doc_inf = NormativeDocuments.objects.all()
    interactiv = Interactive.objects.all()
    laba_obj = Laboratory.objects.all()
    laboratory_two = Laboratories.objects.all()
    questions = Question.objects.all()
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    context = {
        'main_normative_doc_inf': main_normative_doc_inf,
        'interactiv': interactiv,
        'laba_obj': laba_obj,
        'laboratory_two': laboratory_two,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
    }

    return render(request, 'webapp/services/laboratory_services.html', context=context)


def price_lists(request):
    """Services - hygiene_education template"""

    price_lists = PriceLists.objects.all()
    sliders = OurPartners.objects.all()
    interactiv = Interactive.objects.all()
    main_services = Services.objects.all()
    desc_services_title = Services_title.objects.all()
    centre_news = CentreNews.objects.all().order_by('-pub_date')

    context = {
        'price_lists': price_lists,
        'sliders': sliders,
        'interactiv': interactiv,
        'main_services': main_services,
        'desc_services_title': desc_services_title,
        'centre_news': centre_news,
    }

    return render(request, 'webapp/services/price_lists.html', context=context)


def disinfection_disinsection_deratization(request):
    """Services - disinfection_disinsection_deratization template"""
    interactiv = Interactive.objects.all()
    disinfection_info = Disinfection.objects.all()
    deratisation_info = Deratization.objects.all()
    disinsection_info = Disinsection.objects.all()
    disinfection_desc = DisinfectionDesc.objects.all()

    context = {
        'interactiv': interactiv,
        'disinfection_info': disinfection_info,
        'deratisation_info': deratisation_info,
        'disinsection_info': disinsection_info,
        'disinfection_desc': disinfection_desc,
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


def typical_violations_list(request):
    """Activity - typical_violations template"""
    features = Featured.objects.all()
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    all_typical_news = ControlNadzorTipical.objects.all().order_by('-pub_date')
    typical_title = CNadTipicalName.objects.all()

    context = {
        'features': features,
        'interactiv': interactiv,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_title': typical_title,
    }

    return render(request, 'webapp/activity/typical_violations.html', context=context)


def typical_violations_single(request, pk):
    """Views for News details"""
    news_typical = ControlNadzorTipical.objects.filter(pk=pk)
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    typical_inf = ControlNadzorTipical.objects.all()

    all_typical_news = ControlNadzorTipical.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'news_typical': news_typical,
        'interactiv': interactiv,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_inf': typical_inf,
    }
    return render(request, 'webapp/activity/single_typical.html', context=context)


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
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')
    typical_title = CustomProductsName.objects.all()

    context = {
        'features': features,
        'interactiv': interactiv,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_title': typical_title,
    }

    return render(request, 'webapp/activity/custom_products.html', context=context)


def custom_products_single(request, pk):
    """Views for News details"""
    news_typical = CustomProductsInf.objects.filter(pk=pk)
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    typical_inf = CustomProductsInf.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'news_typical': news_typical,
        'interactiv': interactiv,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_inf': typical_inf,
    }
    return render(request, 'webapp/activity/custom_products_single.html', context=context)



def healthy_cities_towns(request):
    """Activity - healthy_cities_towns template"""
    heltitle_inf = HealthyTitle.objects.all()
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    health_inf = Healthy.objects.all()
    cities = Cities.objects.all()
    city_desc = CityDescription.objects.all()
    city_title = CitiesTitle.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'interactiv': interactiv,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'health_inf': health_inf,
        'heltitle_inf': heltitle_inf,
        'cities': cities,
        'city_desc': city_desc,
        'city_title': city_title,
    }

    return render(request, 'webapp/activity/healthy_cities_towns.html', context=context)


def eurasian_economic_union(request):
    """Activity - eurasian_economic_union template"""
    evrz_econom_inf = EconimicSouz.objects.all()
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    typical_inf = CustomProductsInf.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'interactiv': interactiv,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_inf': typical_inf,
        'evrz_econom_inf': evrz_econom_inf,
    }
    return render(request, 'webapp/activity/eurasian_economic_union.html', context=context)


def sanitary_quarantine_points(request):
    """Activity - sanitary_quarantine_points template"""
    evrz_quarantin_inf = Quarantine.objects.all()
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    typical_inf = CustomProductsInf.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'interactiv': interactiv,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_inf': typical_inf,
        'evrz_quarantin_inf': evrz_quarantin_inf,
    }

    return render(request, 'webapp/activity/sanitary_quarantine_points.html', context=context)


def epidemialogic_situations(request):
    """Activity - sanitary_quarantine_points template"""
    evrz_quarantin_inf = EpidemSituations.objects.all()
    interactiv = Interactive.objects.all()
    typical_inf = CustomProductsInf.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')

    context = {
        'interactiv': interactiv,
        'all_typical_news': all_typical_news,
        'typical_inf': typical_inf,
        'evrz_quarantin_inf': evrz_quarantin_inf,
    }

    return render(request, 'webapp/activity/epidemialogic_situations.html', context=context)


def country_registry(request):
    """Activity - sanitary_quarantine_points template"""
    country_reg_inf = CountryRegistry.objects.all()
    interactiv = Interactive.objects.all()
    typical_inf = CustomProductsInf.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')

    context = {
        'interactiv': interactiv,
        'all_typical_news': all_typical_news,
        'typical_inf': typical_inf,
        'country_reg_inf': country_reg_inf,
    }

    return render(request, 'webapp/activity/country_registry.html', context=context)


def resolution(request):
    """Activity - sanitary_quarantine_points template"""
    resolution_inf = Resolution.objects.all()
    interactiv = Interactive.objects.all()
    typical_inf = CustomProductsInf.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')

    context = {
        'interactiv': interactiv,
        'all_typical_news': all_typical_news,
        'typical_inf': typical_inf,
        'resolution_inf': resolution_inf,
    }

    return render(request, 'webapp/activity/resolution.html', context=context)


def epidemiology(request):
    """Activity - epidemiology template"""
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    epidem_title = EpidemialogyName.objects.all()

    all_typical_news = EpidemialogyTipical.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'interactiv': interactiv,
        'epidem_title': epidem_title,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
    }

    return render(request, 'webapp/activity/epidemiology.html', context=context)


def epidemiology_typical(request, pk):
    """Activity - epidemiology template"""
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    typical_inf = EpidemialogyTipical.objects.filter(pk=pk)
    epidem_title = EpidemialogyName.objects.all()


    context = {
        'interactiv': interactiv,
        'epidem_title': epidem_title,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'typical_inf': typical_inf,
    }

    return render(request, 'webapp/activity/epidemialogy_single.html', context=context)


def immunoprophylaxis(request):
    """Activity - immunoprophylaxis template"""
    interactiv = Interactive.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    all_typical_news = ImmunoprophylaxisInf.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'interactiv': interactiv,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
    }

    return render(request, 'webapp/activity/immunoprophylaxis.html', context=context)


def immunoprophylaxis_typical(request, pk):
    """Activity - epidemiology template"""
    interactiv = Interactive.objects.all()
    news_typical = ControlNadzorTipical.objects.filter(pk=pk)
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()
    typical_inf = ImmunoprophylaxisTipical.objects.filter(pk=pk)

    all_typical_news = ImmunoprophylaxisInf.objects.all().order_by('-pub_date')

    # Получаем данные о погоде
    weather = get_weather()

    context = {
        'interactiv': interactiv,
        'news_typical': news_typical,
        'weather': weather,  # Передаем данные о погоде в контекст
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_inf': typical_inf,
    }

    return render(request, 'webapp/activity/immunoprophylaxis_single.html', context=context)


def sustainable_development_goals(request):
    """Activity - sustainable_development_goals template"""
    interactiv = Interactive.objects.all()
    objectives = Objectives.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')
    typical_title = CustomProductsName.objects.all()

    context = {
        'interactiv': interactiv,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_title': typical_title,
        'objectives': objectives,
    }

    return render(request, 'webapp/activity/sustainable_development_goals.html', context=context)


def ticks(request):
    """Activity - sustainable_development_goals template"""

    interactiv = Interactive.objects.all()
    ticks_inf = Ticks.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    title_desc_queans = Question_Ansver_title.objects.all()

    all_typical_news = CustomProductsInf.objects.all().order_by('-pub_date')
    typical_title = CustomProductsName.objects.all()

    context = {
        'interactiv': interactiv,
        'questions': questions,
        'ansvers': ansvers,
        'title_desc_queans': title_desc_queans,
        'all_typical_news': all_typical_news,
        'typical_title': typical_title,
        'ticks_inf': ticks_inf,
    }

    return render(request, 'webapp/activity/ticks.html', context=context)


def analytical_newsletter(request):
    """Activity - analytical_newsletter template"""
    interactiv = Interactive.objects.all()
    see_pdf = InformationAnalytical.objects.all().order_by('-pub_date')
    title_desc_queans = Question_Ansver_title.objects.all()
    questions = Question.objects.all().order_by('-pub_date')
    ansvers = Answer.objects.all()
    sliders = OurPartners.objects.all()

    context = {
        'interactiv': interactiv,
        'see_pdf': see_pdf,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
        'ansvers': ansvers,
        'sliders': sliders,
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
    sliders = OurPartners.objects.all()


    context = {
        'features': features,
        'interactiv': interactiv,
        'see_pdf': see_pdf,
        'title_desc_queans': title_desc_queans,
        'questions': questions,
        'ansvers': ansvers,
        'sliders': sliders,
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


def resurces_slider(request):
    """Recurces slider for main template"""
    sliders = OurPartners.objects.all()

    context = {
        'sliders': sliders,
    }

    return render(request, 'slider/resurces_slider.html', context=context)


def resurces_slider_three(request):
    """Recurces slider for main template"""
    sliders = OurPartners.objects.all()

    context = {
        'sliders': sliders,
    }

    return render(request, 'slider/recurces_slider3.html', context=context)
