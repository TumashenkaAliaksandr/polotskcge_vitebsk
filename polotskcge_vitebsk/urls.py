from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from polotskcge_vitebsk import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Оборачиваем URL-шаблоны в i18n_patterns
urlpatterns += i18n_patterns(
    path('summernote/', include('django_summernote.urls')),
    path('', include('webapp.urls')),
    path('', include('news.urls')),
    # Добавьте здесь другие URL-шаблоны, если необходимо
)
