from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'description_three': CKEditorWidget(),
            'name_li_one': CKEditorWidget(),
            'name_li_two': CKEditorWidget(),
            'name_li_three': CKEditorWidget(),
            'name_li_four': CKEditorWidget(),
            'name_li_five': CKEditorWidget(),
        }

class ResearchesForm(forms.ModelForm):
    class Meta:
        model = Researches
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'description_three': CKEditorWidget(),
            'name_one': CKEditorWidget(),
            'name_two': CKEditorWidget(),
            'name_three': CKEditorWidget(),
        }
