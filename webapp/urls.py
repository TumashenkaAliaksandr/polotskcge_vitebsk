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
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
