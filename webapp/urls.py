from django.urls import path
from webapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


app_name = 'webapp'


urlpatterns = [
    path('', index, name='home'),
    path('chief-doctor/', chief_doctor, name='chief-doctor'),
    path('cge-info/', info_main, name='cge-info'),
    path('cge-news/', news_main, name='cge-news'),
    path('structure/', structure, name='structure'),
    path('working_mode/', working_mode, name='working_mode'),
    path('anti_corruption/', anti_corruption, name='anti_corruption'),
    path('ideological_work/', ideological_work, name='ideological_work'),
    path('charter/', charter, name='charter'),
    path('trade_union/', trade_union, name='trade_union'),
    path('vacancies/', vacancies, name='vacancies'),
    path('appeals/', appeals, name='appeals'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
