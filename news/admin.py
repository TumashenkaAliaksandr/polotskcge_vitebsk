from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from django import forms


class ModelNewsAdminForm(forms.ModelForm):
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
    form = ModelNewsAdminForm
    list_display = ('title', 'description_small', 'description', 'description_company', 'location', 'photo', 'logo_photo',
                    'pub_date', 'author', 'comment_author')

    def author(self, obj):
        return obj.author.username if obj.author else '-'

    author.short_description = 'Author'

    def comment_author(self, obj):
        return obj.comment_author.username if obj.comment_author else '-'

    comment_author.short_description = 'Comment Author'


@admin.register(Interactive)
class InteractiveAdmin(admin.ModelAdmin):
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
    list_display = ('title', 'description', 'photo')
    search_fields = ('title',)
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'photo')
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
