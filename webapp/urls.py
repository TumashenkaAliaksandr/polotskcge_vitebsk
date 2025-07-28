from django.urls import path
from django.views.i18n import set_language
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webapp'

urlpatterns = [
    # A
    path('analytical_newsletter/', analytical_newsletter, name='analytical_newsletter'),
    path('anti_corruption/', anti_corruption, name='anti_corruption'),
    path('appeals/', appeals, name='appeals'),
    path('appeals_normative_documents/', appeals_normative_documents, name='appeals_normative_documents'),
    path('archive/<int:pk>/', archive_single, name='archive_single'),

    # B
    path('book_of_comments/', book_of_comments, name='book_of_comments'),

    # C
    path('cge-info/', info_main, name='cge-info'),
    path('charter/', charter, name='charter'),
    path('check_lists/', check_lists, name='check_lists'),
    path('city/<int:pk>/', city_single, name='city_single'),
    path('contacts/', contacts, name='contacts'),
    path('control_supervisory_activities/', supervisory_activities, name='control_supervisory_activities'),
    path('custom_products/', custom_products, name='custom_products'),
    path('custom_products_single/<int:pk>/', custom_products_single, name='custom_products_single'),

    # D
    path('disinfection_disinsection_deratization/', disinfection_disinsection_deratization, name='disinfection_disinsection_deratization'),
    path('documents_ap/', normative_documents_ap, name='documents_ap'),

    # E
    path('educational_resources/', educational_resources, name='educational_resources'),
    path('electronic_appeals/', electronic_appeals, name='electronic_appeals'),
    path('entity/', structure, name='entity'),
    path('epidemialogy_single/<int:pk>/', epidemiology_typical, name='epidemialogy_single'),
    path('epidemiology/', epidemiology, name='epidemiology'),
    path('eurasian_economic_union/', eurasian_economic_union, name='eurasian_economic_union'),
    path('expertise/', expertise, name='expertise'),

    # H
    path('health_days/', health_days, name='health_days'),
    path('healthy_cities_towns/', healthy_cities_towns, name='healthy_cities_towns'),
    path('healthy_lifestyle/', healthy_lifestyle, name='healthy_lifestyle'),
    path('higher_authority/', higher_authority, name='higher_authority'),
    path('hotline/', hotline, name='hotline'),

    # I
    path('i18n/setlang/', set_language, name='set_language'),
    path('ideological_work/', ideological_work, name='ideological_work'),
    path('immunoprophylaxis/', immunoprophylaxis, name='immunoprophylaxis'),
    path('immunoprophylaxis_single/<int:pk>/', immunoprophylaxis_typical, name='immunoprophylaxis_typical'),
    path('inspection_plan/', inspection_plan, name='inspection_plan'),

    # L
    path('laboratory_offerings/', laboratory_services, name='laboratory_offerings'),

    # M
    path('maintenance_schedule/', maintenance_schedule, name='maintenance_schedule'),
    path('monitoring_plan/', monitoring_plan, name='monitoring_plan'),

    # P
    path('paid_services/', paid_services, name='paid_services'),
    path('paid_services_lawyer/', paid_services_lawyer, name='paid_services_lawyer'),
    path('paid_services_lawyer_single/<int:pk>/', paid_services_lawyer_single, name='paid_services_lawyer_single'),
    path('preventive_measures/', preventive_measures, name='preventive_measures'),
    path('price_lists/', price_lists, name='price_lists'),

    # R
    path('registrations/', registrations, name='registrations'),
    path('regulations/', regulations, name='regulations'),
    path('relation_to_citizens/', relation_to_citizens, name='relation_to_citizens'),
    path('rights_duties/', rights_duties, name='rights_duties'),

    # S
    path('sanitary_quarantine_points/', sanitary_quarantine_points, name='sanitary_quarantine_points'),
    path('services/', services, name='services'),
    path('skp/<int:pk>/', skp, name='skp'),
    path('standart_documents/', standart_documents, name='standart_documents'),
    path('sustainable_development_goals/', sustainable_development_goals, name='sustainable_development_goals'),

    # T
    path('ticks/', ticks, name='ticks'),
    path('trade_union/', trade_union, name='trade_union'),
    path('typical_violations/', typical_violations_list, name='typical_violations'),
    path('typical_violations_single/<int:pk>/', typical_violations_single, name='typical_violations_single'),

    # V
    path('vacancies/', vacancies, name='vacancies'),

    # W
    path('working_mode/', working_mode, name='working_mode'),

    # Root
    path('', index, name='home'),

    path('ajax/search/', ajax_search, name='ajax_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
