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


class Appeals_Form(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    name_two = forms.CharField(widget=CKEditorWidget())
    name_three = forms.CharField(widget=CKEditorWidget())
    appeals_desc = forms.CharField(widget=CKEditorWidget())
    appeals_desc_two = forms.CharField(widget=CKEditorWidget())
    appeals_desc_three = forms.CharField(widget=CKEditorWidget())
    appeals_desc_four = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = MainAppeals
        fields = ('name', 'name_two', 'name_three', 'appeals_desc', 'appeals_desc_two', 'appeals_desc_three', 'appeals_desc_four')


class AnticorrTitleForm(forms.ModelForm):

    name = forms.CharField(label='Имя', widget=CKEditorWidget())
    desс_anticorr = forms.CharField(label='Описание под тайтл Анткоррупция', widget=CKEditorWidget())

    class Meta:
        model = AnticorrTitle
        fields = ('name', 'desс_anticorr')


class AnticorrForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=CKEditorWidget())
    description = forms.CharField(widget=CKEditorWidget())
    link = forms.URLField(label='Ссылка')
    icon_class = forms.CharField(max_length=100, label='Класс иконки')

    class Meta:
        model = Anticorr
        fields = ('name', 'description', 'link', 'icon_class')


class Up_Organ_Form(forms.ModelForm):
    reception_time = forms.CharField(widget=CKEditorWidget())
    post = forms.CharField(widget=CKEditorWidget())
    name = forms.CharField(widget=CKEditorWidget())
    phone = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Up_Organ
        fields = ('name', 'post', 'phone', 'reception_time')


class NormativeDocuments_Form(forms.ModelForm):
    name = forms.CharField(widget=CKEditorWidget())
    normative_desc = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = NormativeDocuments
        fields = ('name', 'normative_desc')


class LabaForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'description_three': CKEditorWidget(),
            'name_li_one': CKEditorWidget(),
            'name_li_two': CKEditorWidget(),
            'name_li_three': CKEditorWidget(),
            'name_li_four': CKEditorWidget(),
            'name_li_five': CKEditorWidget(),
            'name_li_six': CKEditorWidget(),
            'name_two': CKEditorWidget(),
            'name_three': CKEditorWidget(),
        }


class LaboratoriesForm(forms.ModelForm):
    class Meta:
        model = Laboratories
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'description': CKEditorWidget(),
        }


class ApRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'description_three': CKEditorWidget(),
        }


class RelationForm(forms.ModelForm):
    class Meta:
        model = Relation
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'description': CKEditorWidget(),
        }


class HumanResourcesDescForm(forms.ModelForm):
    class Meta:
        model = HumanResourcesDesc
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'description': CKEditorWidget(),
        }


class HumanResourcesForm(forms.ModelForm):
    class Meta:
        model = HumanResources
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'number_ap': CKEditorWidget(),
            'name_ap': CKEditorWidget(),
            'size_ap': CKEditorWidget(),
            'doc_ap': CKEditorWidget(),
        }


class AccountingDescForm(forms.ModelForm):
    class Meta:
        model = AccountingDesc
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'description': CKEditorWidget(),
        }


class AccountingForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'number_ap': CKEditorWidget(),
            'name_ap': CKEditorWidget(),
            'size_ap': CKEditorWidget(),
            'doc_ap': CKEditorWidget(),
            'date_ap': CKEditorWidget(),
        }


class UnionDescForm(forms.ModelForm):

    class Meta:
        model = UnionDesc
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'description': CKEditorWidget(),
        }


class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'number_ap': CKEditorWidget(),
            'name_ap': CKEditorWidget(),
            'size_ap': CKEditorWidget(),
            'doc_ap': CKEditorWidget(),
            'date_ap': CKEditorWidget(),
        }


class ListingDecreeDescForm(forms.ModelForm):
    class Meta:
        model = UnionDesc
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'description': CKEditorWidget(),
        }


class ListingDecreeForm(forms.ModelForm):
    class Meta:
        model = ListingDecree
        fields = '__all__'
        widgets = {
            'name': CKEditorWidget(),
            'number_ap': CKEditorWidget(),
            'name_ap': CKEditorWidget(),
            'size_ap': CKEditorWidget(),
            'doc_ap': CKEditorWidget(),
            'date_ap': CKEditorWidget(),
        }


class ProfsouzForm(forms.ModelForm):
    class Meta:
        model = Profsouz
        fields = '__all__'
        widgets = {
            'number': CKEditorWidget(),
            'name_doctors': CKEditorWidget(),
            'status': CKEditorWidget(),
            'phone': CKEditorWidget(),
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
        }


class ProfsouzTwoForm(forms.ModelForm):
    class Meta:
        model = ProfsouzTwo
        fields = '__all__'
        widgets = {
            'number': CKEditorWidget(),
            'name_doctors': CKEditorWidget(),
            'status': CKEditorWidget(),
            'phone': CKEditorWidget(),
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
        }


class ProfsouzDescForm(forms.ModelForm):
    class Meta:
        model = ProfsouzDesc
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'package': CKEditorWidget(),
        }


class ProfsouzIconsForm(forms.ModelForm):
    class Meta:
        model = ProfsouzIcons
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
        }


class ProfsouzDescOneForm(forms.ModelForm):
    class Meta:
        model = ProfsouzDescOne
        fields = '__all__'
        widgets = {
            'name_main': CKEditorWidget(),
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'package': CKEditorWidget(),
        }


class DisinfectionForm(forms.ModelForm):
    class Meta:
        model = Disinfection
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'name_main': CKEditorWidget(),
        }

class DeratizationForm(forms.ModelForm):
    class Meta:
        model = Deratization
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'name_main': CKEditorWidget(),
        }


class DisinsectionForm(forms.ModelForm):
    class Meta:
        model = Disinsection
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'name_main': CKEditorWidget(),
        }


class DisinfectionDescForm(forms.ModelForm):
    class Meta:
        model = DisinfectionDesc
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'description_two': CKEditorWidget(),
            'name_main': CKEditorWidget(),
        }
