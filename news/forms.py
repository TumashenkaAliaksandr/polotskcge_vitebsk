from django import forms
from django_summernote.widgets import SummernoteWidget
from news.models import ModelNews


class ModelNewsForm(forms.ModelForm):
    class Meta:
        model = ModelNews
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_small': SummernoteWidget(),
            'description_company': SummernoteWidget(),
        }
