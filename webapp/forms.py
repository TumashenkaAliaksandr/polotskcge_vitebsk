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


class ZojForm(forms.ModelForm):
    class Meta:
        model = Zoj
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
        widgets = {
            'description': CKEditorWidget(),
        }


class Book_complaintForm(forms.ModelForm):
    class Meta:
        model = Book_complaint
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }


class ReceptionHoursForm(forms.ModelForm):
    class Meta:
        model = ReceptionHours
        fields = '__all__'


class GeneralInfoForm(forms.ModelForm):
    class Meta:
        model = GeneralInfo
        fields = ['title', 'description']  # Включаем поле description в форму


class EducationalResourceAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = EducationalResource
        fields = '__all__'


class HotlineHoursForm(forms.ModelForm):
    reception_time = forms.CharField(widget=CKEditorWidget())
    post = forms.CharField(widget=CKEditorWidget())
    name = forms.CharField(widget=CKEditorWidget())
    phone = forms.CharField(widget=CKEditorWidget())
    date_hotline = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = HotlineHours
        fields = ('name', 'post', 'phone', 'reception_time', 'date_hotline')


class HotlineHours_TitleForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = HotlineHours_Title
        fields = ('name', 'description')


class HotlineHours_Title_descForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = HotlineHours_Title
        fields = ('name', 'description')


class Electronic_appeals_Title_descForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Electronic_appeals_Title_desc
        fields = ('name', 'description')


class Organ_Title_descForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Organ_Title_desc
        fields = ('name', 'description')


class Up_Organ_infForm(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Organ_Title_desc
        fields = ('name', 'description')


class Expertise_Form(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())
    description_two = forms.CharField(widget=CKEditorWidget())
    description_three = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Expertise
        fields = ('name', 'description', 'description_two', 'description_three')


class Duties_Form(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Duties
        fields = ('name', 'description')


class MaintenanceSh_Form(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = MaintenanceSchedule
        fields = ('name', 'description')


class Vacancies_Form(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    vacancy = forms.CharField(widget=CKEditorWidget())
    vacancy_two = forms.CharField(widget=CKEditorWidget())
    vacancy_three = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Vacancies
        fields = ('name', 'vacancy', 'vacancy_two', 'vacancy_three')


class Up_Organ_Form(forms.ModelForm):
    reception_time = forms.CharField(widget=CKEditorWidget())
    post = forms.CharField(widget=CKEditorWidget())
    name = forms.CharField(widget=CKEditorWidget())
    phone = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Up_Organ
        fields = ('name', 'post', 'phone', 'reception_time')
