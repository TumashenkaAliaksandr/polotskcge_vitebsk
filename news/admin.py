from django.contrib import admin
from .models import ModelNews
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
