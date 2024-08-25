from django import forms
from tinymce.widgets import TinyMCE
from news.models import ModelNews


class ModelNewsForm(forms.ModelForm):
    class Meta:
        model = ModelNews
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_small': TinyMCE(),
            'description_company': TinyMCE(),
        }
