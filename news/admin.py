from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms


class ModelNewsAdminForm(forms.ModelForm):
    """Форма администратора для модели ModelNews."""
    class Meta:
        model = ModelNews
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_company': CKEditorWidget(),
            'description_small': CKEditorWidget(),
            'comment': CKEditorWidget(),
        }


@admin.register(ModelNews)
class BlogNewsAdmin(admin.ModelAdmin):
    """Администратор модели ModelNews."""
    form = ModelNewsAdminForm
    list_display = ('title', 'description_small', 'description', 'description_company', 'location', 'photo', 'logo_photo',
                    'pub_date', 'author', 'comment_author', 'is_popular', 'is_nature_news', 'is_health_news', 'is_sport_news',
                    'is_economic_news', 'is_main_news', 'is_main_measures', 'is_main_days_health')

    def author(self, obj):
        return obj.author.username if obj.author else '-'

    author.short_description = 'Author'

    def comment_author(self, obj):
        return obj.comment_author.username if obj.comment_author else '-'

    comment_author.short_description = 'Comment Author'


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
        models.TextField: {'widget': CKEditorWidget}
    }


@admin.register(PreviewNews)
class PreviewNewsAdmin(admin.ModelAdmin):
    """Администратор предварительных новостей."""
    list_display = ('title', 'description', 'photo', 'is_popular', 'is_nature_news', 'is_health_news', 'is_sport_news',
                    'is_economic_news', 'is_main_news')
    search_fields = ('title',)
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'photo', 'is_popular', 'is_nature_news', 'is_health_news', 'is_sport_news',
                    'is_economic_news', 'is_main_news')
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


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
