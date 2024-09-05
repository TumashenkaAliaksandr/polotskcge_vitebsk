from django import forms
from django_summernote.widgets import SummernoteWidget
from tinymce.widgets import TinyMCE

from .models import *



class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'description_three': SummernoteWidget(),
            'name_li_one': SummernoteWidget(),
            'name_li_two': SummernoteWidget(),
            'name_li_three': SummernoteWidget(),
            'name_li_four': SummernoteWidget(),
            'name_li_five': SummernoteWidget(),
        }


class ZojForm(forms.ModelForm):
    class Meta:
        model = Zoj
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'description_three': SummernoteWidget(),
            'name_li_one': SummernoteWidget(),
            'name_li_two': SummernoteWidget(),
            'name_li_three': SummernoteWidget(),
            'name_li_four': SummernoteWidget(),
            'name_li_five': SummernoteWidget(),
        }


class ResearchesForm(forms.ModelForm):
    class Meta:
        model = Researches
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'description_three': SummernoteWidget(),
            'description_four': SummernoteWidget(),
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
            'description': SummernoteWidget(),
        }


class Book_complaintForm(forms.ModelForm):
    class Meta:
        model = Book_complaint
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
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
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = EducationalResource
        fields = '__all__'


class InformationAnalyticalForm(forms.ModelForm):

    class Meta:
        model = InformationAnalytical
        fields = '__all__'


class HotlineHoursForm(forms.ModelForm):
    reception_time = forms.CharField(widget=TinyMCE())
    post = forms.CharField(widget=TinyMCE())
    name = forms.CharField(widget=TinyMCE())
    phone = forms.CharField(widget=TinyMCE())
    date_hotline = forms.CharField(widget=TinyMCE())

    class Meta:
        model = HotlineHours
        fields = ('name', 'post', 'phone', 'reception_time', 'date_hotline')


class HotlineHours_TitleForm(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = HotlineHours_Title
        fields = ('name', 'description')


class HotlineHours_Title_descForm(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = HotlineHours_Title
        fields = ('name', 'description')


class Electronic_appeals_Title_descForm(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Electronic_appeals_Title_desc
        fields = ('name', 'description')


class Organ_Title_descForm(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Organ_Title_desc
        fields = ('name', 'description')


class Up_Organ_infForm(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Organ_Title_desc
        fields = ('name', 'description')


class Expertise_Form(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())
    description_two = forms.CharField(widget=TinyMCE())
    description_three = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Expertise
        fields = ('name', 'description', 'description_two', 'description_three')


class Duties_Form(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Duties
        fields = ('name', 'description')


class MaintenanceSh_Form(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())

    class Meta:
        model = MaintenanceSchedule
        fields = ('name', 'description')


class Vacancies_Form(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    vacancy = forms.CharField(widget=TinyMCE())
    vacancy_two = forms.CharField(widget=TinyMCE())
    vacancy_three = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Vacancies
        fields = ('name', 'vacancy', 'vacancy_two', 'vacancy_three')


class Appeals_Form(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    name_two = forms.CharField(widget=TinyMCE())
    name_three = forms.CharField(widget=TinyMCE())
    appeals_desc = forms.CharField(widget=TinyMCE())
    appeals_desc_two = forms.CharField(widget=TinyMCE())
    appeals_desc_three = forms.CharField(widget=TinyMCE())
    appeals_desc_four = forms.CharField(widget=TinyMCE())

    class Meta:
        model = MainAppeals
        fields = ('name', 'name_two', 'name_three', 'appeals_desc', 'appeals_desc_two', 'appeals_desc_three', 'appeals_desc_four')


class AnticorrTitleForm(forms.ModelForm):

    name = forms.CharField(label='Имя', widget=TinyMCE())
    desс_anticorr = forms.CharField(label='Описание под тайтл Анткоррупция', widget=TinyMCE())

    class Meta:
        model = AnticorrTitle
        fields = ('name', 'desс_anticorr')


class AnticorrForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=TinyMCE())
    description = forms.CharField(widget=TinyMCE())
    link = forms.URLField(label='Ссылка')
    icon_class = forms.CharField(max_length=100, label='Класс иконки')

    class Meta:
        model = Anticorr
        fields = ('name', 'description', 'link', 'icon_class')


class Up_Organ_Form(forms.ModelForm):
    reception_time = forms.CharField(widget=TinyMCE())
    post = forms.CharField(widget=TinyMCE())
    name = forms.CharField(widget=TinyMCE())
    phone = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Up_Organ
        fields = ('name', 'post', 'phone', 'reception_time')


class NormativeDocuments_Form(forms.ModelForm):
    name = forms.CharField(widget=TinyMCE())
    normative_desc = forms.CharField(widget=TinyMCE())

    class Meta:
        model = NormativeDocuments
        fields = ('name', 'normative_desc')


class EconimicSouz_Form(forms.ModelForm):
    name_main = forms.CharField(widget=TinyMCE())
    name = forms.CharField(widget=TinyMCE())
    desc = forms.CharField(widget=TinyMCE())

    class Meta:
        model = EconimicSouz
        fields = ('name_main', 'name', 'desc', 'pdf_file', 'link', 'icon_class')


class QuarantineForm(forms.ModelForm):
    name_main = forms.CharField(widget=TinyMCE())
    name = forms.CharField(widget=TinyMCE())
    desc = forms.CharField(widget=TinyMCE())
    desc_two = forms.CharField(widget=TinyMCE())

    class Meta:
        model = EconimicSouz
        fields = ('name_main', 'name', 'desc', 'desc_two', 'pdf_file', 'link', 'icon_class')


class EpidemialSituationsForm(forms.ModelForm):
    class Meta:
        model = EpidemSituations
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'desc': SummernoteWidget(),
        }


class CountryRegistryForm(forms.ModelForm):
    class Meta:
        model = CountryRegistry
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'desc': SummernoteWidget(),
        }


class HealthyTitleForm(forms.ModelForm):
    class Meta:
        model = HealthyTitle
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
        }


class HealthyForm(forms.ModelForm):
    class Meta:
        model = Healthy
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'name_taitle': SummernoteWidget(),
        }



class ResolutionForm(forms.ModelForm):
    class Meta:
        model = Resolution
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'desc': SummernoteWidget(),
        }


class LabaForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'description_three': SummernoteWidget(),
            'name_li_one': SummernoteWidget(),
            'name_li_two': SummernoteWidget(),
            'name_li_three': SummernoteWidget(),
            'name_li_four': SummernoteWidget(),
            'name_li_five': SummernoteWidget(),
            'name_li_six': SummernoteWidget(),
            'name_two': SummernoteWidget(),
            'name_three': SummernoteWidget(),
        }


class LaboratoriesForm(forms.ModelForm):
    class Meta:
        model = Laboratories
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
        }


class ApRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'description_three': SummernoteWidget(),
        }


class RelationForm(forms.ModelForm):
    class Meta:
        model = Relation
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
        }


class HumanResourcesDescForm(forms.ModelForm):
    class Meta:
        model = HumanResourcesDesc
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
        }


class HumanResourcesForm(forms.ModelForm):
    class Meta:
        model = HumanResources
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'number_ap': SummernoteWidget(),
            'name_ap': SummernoteWidget(),
            'size_ap': SummernoteWidget(),
            'doc_ap': SummernoteWidget(),
        }


class AccountingDescForm(forms.ModelForm):
    class Meta:
        model = AccountingDesc
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
        }


class AccountingForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'number_ap': SummernoteWidget(),
            'name_ap': SummernoteWidget(),
            'size_ap': SummernoteWidget(),
            'doc_ap': SummernoteWidget(),
            'date_ap': SummernoteWidget(),
        }


class UnionDescForm(forms.ModelForm):

    class Meta:
        model = UnionDesc
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
        }


class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'number_ap': SummernoteWidget(),
            'name_ap': SummernoteWidget(),
            'size_ap': SummernoteWidget(),
            'doc_ap': SummernoteWidget(),
            'date_ap': SummernoteWidget(),
        }


class ListingDecreeDescForm(forms.ModelForm):
    class Meta:
        model = UnionDesc
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'description': SummernoteWidget(),
        }


class ListingDecreeForm(forms.ModelForm):
    class Meta:
        model = ListingDecree
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'number_ap': SummernoteWidget(),
            'name_ap': SummernoteWidget(),
            'size_ap': SummernoteWidget(),
            'doc_ap': SummernoteWidget(),
            'date_ap': SummernoteWidget(),
        }


class ProfsouzForm(forms.ModelForm):
    class Meta:
        model = Profsouz
        fields = '__all__'
        widgets = {
            'number': SummernoteWidget(),
            'name_doctors': SummernoteWidget(),
            'status': SummernoteWidget(),
            'phone': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
        }


class ProfsouzTwoForm(forms.ModelForm):
    class Meta:
        model = ProfsouzTwo
        fields = '__all__'
        widgets = {
            'number': SummernoteWidget(),
            'name_doctors': SummernoteWidget(),
            'status': SummernoteWidget(),
            'phone': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
        }


class ProfsouzDescForm(forms.ModelForm):
    class Meta:
        model = ProfsouzDesc
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'package': SummernoteWidget(),
        }


class ProfsouzIconsForm(forms.ModelForm):
    class Meta:
        model = ProfsouzIcons
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
        }


class ProfsouzDescOneForm(forms.ModelForm):
    class Meta:
        model = ProfsouzDescOne
        fields = '__all__'
        widgets = {
            'name_main': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'package': SummernoteWidget(),
        }


class DisinfectionForm(forms.ModelForm):
    class Meta:
        model = Disinfection
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'name_main': SummernoteWidget(),
        }

class DeratizationForm(forms.ModelForm):
    class Meta:
        model = Deratization
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'name_main': SummernoteWidget(),
        }


class DisinsectionForm(forms.ModelForm):
    class Meta:
        model = Disinsection
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'name_main': SummernoteWidget(),
        }


class DisinfectionDescForm(forms.ModelForm):
    class Meta:
        model = DisinfectionDesc
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'name_main': SummernoteWidget(),
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'name_main': SummernoteWidget(),
        }


class BlanksInventoryForm(forms.ModelForm):
    class Meta:
        model = BlanksInventory
        fields = '__all__'
        widgets = {
            'name_for_blanks': SummernoteWidget(),
            'blanks_all': SummernoteWidget(),
        }


class ControlNadzorTipicalForm(forms.ModelForm):
    class Meta:
        model = ControlNadzorTipical
        fields = '__all__'
        widgets = {
            'number': SummernoteWidget(),
            'objects_control': SummernoteWidget(),
            'typical_violations': SummernoteWidget(),
            'name_typical_violations': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'description_three': SummernoteWidget(),
            'name_typical': SummernoteWidget(),
            'name': SummernoteWidget(),
        }


class CNadTipicalNameForm(forms.ModelForm):
    class Meta:
        model = CNadTipicalName
        fields = '__all__'
        widgets = {
            'name_typical': SummernoteWidget(),
        }


class CustomProductsInfForm(forms.ModelForm):
    class Meta:
        model = CustomProductsInf
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_small': SummernoteWidget(),
            'name_typical': SummernoteWidget(),
            'name': SummernoteWidget(),
        }


class CustomProductsNameForm(forms.ModelForm):
    class Meta:
        model = CustomProductsName
        fields = '__all__'
        widgets = {
            'name_typical': SummernoteWidget(),
        }


class EpidemialogyNameForm(forms.ModelForm):
    class Meta:
        model = CNadTipicalName
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
        }


class ServicesLawyerNameForm(forms.ModelForm):
    class Meta:
        model = ServicesLawyerName
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
        }


class EpidemialogyTipicalForm(forms.ModelForm):
    class Meta:
        model = EpidemialogyTipical
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'name_epidem': SummernoteWidget(),
            'description_small': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description2': SummernoteWidget(),
        }


class ServicesLawyerTipicalForm(forms.ModelForm):
    class Meta:
        model = ServicesLawyerTipical
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'name_lawyer': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
        }


class ContactInfoHadForm(forms.ModelForm):
    class Meta:
        model = ContactInfoHad
        fields = '__all__'
        widgets = {
            'working_days': SummernoteWidget(),
            'lunch_time': SummernoteWidget(),
            'phone_number': SummernoteWidget(),
            'email_address': SummernoteWidget(),
        }


class ImmunoprophylaxisNameForm(forms.ModelForm):
    class Meta:
        model = ImmunoprophylaxisName
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
        }


class ImmunoprophylaxisInfForm(forms.ModelForm):
    class Meta:
        model = ImmunoprophylaxisInf
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'name': SummernoteWidget(),
        }



class ImmunoprophylaxisTipicalForm(forms.ModelForm):
    class Meta:
        model = ImmunoprophylaxisTipical
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'name_two': SummernoteWidget(),
            'name_three': SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'description_three': SummernoteWidget(),
        }


class ObjectivesForm(forms.ModelForm):
    class Meta:
        model = Objectives
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'name': SummernoteWidget(),
        }


class TicksForm(forms.ModelForm):
    class Meta:
        model = Ticks
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'name': SummernoteWidget(),
            'name_map': SummernoteWidget(),
        }


class StudiesForm(forms.ModelForm):
    class Meta:
        model = Studies
        fields = '__all__'
        widgets = {
            'desc': SummernoteWidget(),
            'indicators': SummernoteWidget(),
            'catering_workers': SummernoteWidget(),
            'name': SummernoteWidget(),
            'after_workers': SummernoteWidget(),
            'employees_school': SummernoteWidget(),
        }


class WaterQualitySafetyForm(forms.ModelForm):
    class Meta:
        model = WaterQualitySafety
        fields = '__all__'
        widgets = {
            'desc': SummernoteWidget(),
            'indicators': SummernoteWidget(),
            'mine_well': SummernoteWidget(),
            'name': SummernoteWidget(),
            'basic': SummernoteWidget(),
            'standart': SummernoteWidget(),
            'standart_plus': SummernoteWidget(),
        }


class LaboratoryFruitVegetableForm(forms.ModelForm):
    class Meta:
        model = LaboratoryFruitVegetable
        fields = '__all__'
        widgets = {
            'desc': SummernoteWidget(),
            'cost': SummernoteWidget(),
            'name': SummernoteWidget(),
            'paket': SummernoteWidget(),
        }


class EripPaymentForm(forms.ModelForm):
    class Meta:
        model = EripPayment
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'description_two': SummernoteWidget(),
            'payment_methods': SummernoteWidget(),
            'name': SummernoteWidget(),
            'unp': SummernoteWidget(),
            'title_portal': SummernoteWidget(),
        }


class PhotoDayForm(forms.ModelForm):
    class Meta:
        model = PhotoDay
        fields = '__all__'
        widgets = {
            'description': SummernoteWidget(),
            'name': SummernoteWidget(),
        }


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'adres': SummernoteWidget(),
            'mail': SummernoteWidget(),
            'phone': SummernoteWidget(),
        }


class CentreNewsForm(forms.ModelForm):
    class Meta:
        model = CentreNews
        fields = '__all__'
        widgets = {
            'name': SummernoteWidget(),
            'desc': SummernoteWidget(),
            'desc_hover': SummernoteWidget(),
            'author': SummernoteWidget(),
        }
