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
            'description_four': CKEditorWidget(),
            'icon_class': forms.TextInput(),
            'icon_class_two': forms.TextInput(),
            'icon_class_three': forms.TextInput(),
            'icon_class_four': forms.TextInput(),
        }


class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = '__all__'

class FeaturedForm(forms.ModelForm):
    class Meta:
        model = Featured
        fields = '__all__'
