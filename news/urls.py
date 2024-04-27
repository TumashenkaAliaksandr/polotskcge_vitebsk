from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('news/', news, name='news'),
    path('single/<int:pk>/', NewsDetailView, name='single'),
]