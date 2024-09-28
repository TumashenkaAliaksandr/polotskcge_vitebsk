from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('cge_news/', cge_news, name='cge_news'),
    path('single/<int:pk>/', NewsDetailView, name='single'),
]
