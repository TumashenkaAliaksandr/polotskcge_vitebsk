from django import forms
from ckeditor.widgets import CKEditorWidget
from news.models import ModelNews


class ModelNewsForm(forms.ModelForm):
    class Meta:
        model = ModelNews
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_small': CKEditorWidget(),
            'description_company': CKEditorWidget(),
        }
