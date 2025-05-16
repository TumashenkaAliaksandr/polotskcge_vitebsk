from django.contrib import admin
from django.utils.html import format_html, strip_tags
from django_summernote.widgets import SummernoteWidget

from webapp.forms import PreviewNewsForm
from .forms import ModelNewsForm
from .models import *
from tinymce.widgets import TinyMCE
from django import forms


class ModelNewsAdminForm(forms.ModelForm):
    """Форма администратора для модели ModelNews."""
    class Meta:
        model = ModelNews
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_company': SummernoteWidget(),
            'description_small': SummernoteWidget(),
            'comment': SummernoteWidget(),
        }


@admin.register(ModelNews)
class BlogNewsAdmin(admin.ModelAdmin):
    form = ModelNewsForm
    list_display = ('title', 'slug', 'location', 'display_photo', 'display_logo_photo', 'pub_date', 'author', 'comment_author', 'is_popular', 'is_nature_news', 'is_health_news', 'is_sport_news', 'is_economic_news', 'is_main_news', 'is_main_measures', 'is_main_days_health')

    def author(self, obj):
        return obj.author.username if obj.author else '-'
    author.short_description = 'Author'

    def comment_author(self, obj):
        return obj.comment_author.username if obj.comment_author else '-'
    comment_author.short_description = 'Comment Author'

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-width: 100px; height: auto;" />', obj.photo.url)
        return "No Photo"
    display_photo.short_description = 'Фото Главное'

    def display_logo_photo(self, obj):
        if obj.logo_photo:
            return format_html('<img src="{}" style="max-width: 100px; height: auto;" />', obj.logo_photo.url)
        return "No Logo Photo"

    display_logo_photo.short_description = 'Маленькое Фото'


@admin.register(Interactive)
class InteractiveAdmin(admin.ModelAdmin):
    """Администратор интерактивной модели."""
    list_display = ('name', 'description', 'description_two')
    search_fields = ('name',)
    list_filter = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'description_two')
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget}
    }


# @admin.register(PreviewNews)
# class PreviewNewsAdmin(admin.ModelAdmin):
#     """Администратор предварительных новостей."""
#     list_display = ('title', 'photo', 'description', 'is_popular', 'is_nature_news', 'is_health_news', 'is_sport_news',
#                     'is_economic_news', 'is_main_news')
#     search_fields = ('title',)
#     list_filter = ('title',)
#     fieldsets = (
#         (None, {
#             'fields': ('title', 'photo', 'is_popular', 'is_nature_news', 'is_health_news', 'is_sport_news',
#                     'is_economic_news', 'is_main_news')
#         }),
#     )
#     formfield_overrides = {
#         models.TextField: {'widget': SummernoteWidget}
#     }


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    """Администратор видео."""
    list_display = ('title', 'author', 'timestamp', 'is_featured')
    search_fields = ('title', 'author', 'category')
    fieldsets = (
        (None, {
            'fields': ('title', 'video_file', 'description', 'author', 'category', 'is_featured')
        }),
    )


@admin.register(PreviewNews)
class PreviewNewsAdmin(admin.ModelAdmin):
    form = PreviewNewsForm

    def clean_name(self, obj):
        return strip_tags(obj.title)

    clean_name.short_description = 'Title'
    list_display = ['clean_name']

