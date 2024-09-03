from django import forms
from tinymce.widgets import TinyMCE

from .models import *



class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'description_three': TinyMCE(),
            'name_li_one': TinyMCE(),
            'name_li_two': TinyMCE(),
            'name_li_three': TinyMCE(),
            'name_li_four': TinyMCE(),
            'name_li_five': TinyMCE(),
        }


class ZojForm(forms.ModelForm):
    class Meta:
        model = Zoj
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'description_three': TinyMCE(),
            'name_li_one': TinyMCE(),
            'name_li_two': TinyMCE(),
            'name_li_three': TinyMCE(),
            'name_li_four': TinyMCE(),
            'name_li_five': TinyMCE(),
        }


class ResearchesForm(forms.ModelForm):
    class Meta:
        model = Researches
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'description_three': TinyMCE(),
            'description_four': TinyMCE(),
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
            'description': TinyMCE(),
        }


class Book_complaintForm(forms.ModelForm):
    class Meta:
        model = Book_complaint
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
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
            'name': TinyMCE(),
            'desc': TinyMCE(),
        }


class CountryRegistryForm(forms.ModelForm):
    class Meta:
        model = CountryRegistry
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'desc': TinyMCE(),
        }


class HealthyTitleForm(forms.ModelForm):
    class Meta:
        model = HealthyTitle
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
        }


class HealthyForm(forms.ModelForm):
    class Meta:
        model = Healthy
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'name_taitle': TinyMCE(),
        }



class ResolutionForm(forms.ModelForm):
    class Meta:
        model = Resolution
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'desc': TinyMCE(),
        }


class LabaForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'description_three': TinyMCE(),
            'name_li_one': TinyMCE(),
            'name_li_two': TinyMCE(),
            'name_li_three': TinyMCE(),
            'name_li_four': TinyMCE(),
            'name_li_five': TinyMCE(),
            'name_li_six': TinyMCE(),
            'name_two': TinyMCE(),
            'name_three': TinyMCE(),
        }


class LaboratoriesForm(forms.ModelForm):
    class Meta:
        model = Laboratories
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
        }


class ApRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'description_three': TinyMCE(),
        }


class RelationForm(forms.ModelForm):
    class Meta:
        model = Relation
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
        }


class HumanResourcesDescForm(forms.ModelForm):
    class Meta:
        model = HumanResourcesDesc
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
        }


class HumanResourcesForm(forms.ModelForm):
    class Meta:
        model = HumanResources
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'number_ap': TinyMCE(),
            'name_ap': TinyMCE(),
            'size_ap': TinyMCE(),
            'doc_ap': TinyMCE(),
        }


class AccountingDescForm(forms.ModelForm):
    class Meta:
        model = AccountingDesc
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
        }


class AccountingForm(forms.ModelForm):
    class Meta:
        model = Accounting
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'number_ap': TinyMCE(),
            'name_ap': TinyMCE(),
            'size_ap': TinyMCE(),
            'doc_ap': TinyMCE(),
            'date_ap': TinyMCE(),
        }


class UnionDescForm(forms.ModelForm):

    class Meta:
        model = UnionDesc
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
        }


class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'number_ap': TinyMCE(),
            'name_ap': TinyMCE(),
            'size_ap': TinyMCE(),
            'doc_ap': TinyMCE(),
            'date_ap': TinyMCE(),
        }


class ListingDecreeDescForm(forms.ModelForm):
    class Meta:
        model = UnionDesc
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'description': TinyMCE(),
        }


class ListingDecreeForm(forms.ModelForm):
    class Meta:
        model = ListingDecree
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'number_ap': TinyMCE(),
            'name_ap': TinyMCE(),
            'size_ap': TinyMCE(),
            'doc_ap': TinyMCE(),
            'date_ap': TinyMCE(),
        }


class ProfsouzForm(forms.ModelForm):
    class Meta:
        model = Profsouz
        fields = '__all__'
        widgets = {
            'number': TinyMCE(),
            'name_doctors': TinyMCE(),
            'status': TinyMCE(),
            'phone': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
        }


class ProfsouzTwoForm(forms.ModelForm):
    class Meta:
        model = ProfsouzTwo
        fields = '__all__'
        widgets = {
            'number': TinyMCE(),
            'name_doctors': TinyMCE(),
            'status': TinyMCE(),
            'phone': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
        }


class ProfsouzDescForm(forms.ModelForm):
    class Meta:
        model = ProfsouzDesc
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'package': TinyMCE(),
        }


class ProfsouzIconsForm(forms.ModelForm):
    class Meta:
        model = ProfsouzIcons
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
        }


class ProfsouzDescOneForm(forms.ModelForm):
    class Meta:
        model = ProfsouzDescOne
        fields = '__all__'
        widgets = {
            'name_main': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'package': TinyMCE(),
        }


class DisinfectionForm(forms.ModelForm):
    class Meta:
        model = Disinfection
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'name_main': TinyMCE(),
        }

class DeratizationForm(forms.ModelForm):
    class Meta:
        model = Deratization
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'name_main': TinyMCE(),
        }


class DisinsectionForm(forms.ModelForm):
    class Meta:
        model = Disinsection
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'name_main': TinyMCE(),
        }


class DisinfectionDescForm(forms.ModelForm):
    class Meta:
        model = DisinfectionDesc
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'name_main': TinyMCE(),
        }


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'name_main': TinyMCE(),
        }


class ControlNadzorTipicalForm(forms.ModelForm):
    class Meta:
        model = ControlNadzorTipical
        fields = '__all__'
        widgets = {
            'number': TinyMCE(),
            'objects_control': TinyMCE(),
            'typical_violations': TinyMCE(),
            'name_typical_violations': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'description_three': TinyMCE(),
            'name_typical': TinyMCE(),
            'name': TinyMCE(),
        }


class CNadTipicalNameForm(forms.ModelForm):
    class Meta:
        model = CNadTipicalName
        fields = '__all__'
        widgets = {
            'name_typical': TinyMCE(),
        }


class CustomProductsInfForm(forms.ModelForm):
    class Meta:
        model = CustomProductsInf
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'name_typical': TinyMCE(),
            'name': TinyMCE(),
        }


class CustomProductsNameForm(forms.ModelForm):
    class Meta:
        model = CustomProductsName
        fields = '__all__'
        widgets = {
            'name_typical': TinyMCE(),
        }


class EpidemialogyNameForm(forms.ModelForm):
    class Meta:
        model = CNadTipicalName
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
        }


class ServicesLawyerNameForm(forms.ModelForm):
    class Meta:
        model = ServicesLawyerName
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
        }


class EpidemialogyTipicalForm(forms.ModelForm):
    class Meta:
        model = EpidemialogyTipical
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'name_epidem': TinyMCE(),
            'name_two': TinyMCE(),
            'name_three': TinyMCE(),
            'description_small': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'description_three': TinyMCE(),
        }


class ServicesLawyerTipicalForm(forms.ModelForm):
    class Meta:
        model = ServicesLawyerTipical
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'name_lawyer': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
        }


class ContactInfoHadForm(forms.ModelForm):
    class Meta:
        model = ContactInfoHad
        fields = '__all__'
        widgets = {
            'working_days': TinyMCE(),
            'lunch_time': TinyMCE(),
            'phone_number': TinyMCE(),
            'email_address': TinyMCE(),
        }


class ImmunoprophylaxisNameForm(forms.ModelForm):
    class Meta:
        model = ImmunoprophylaxisName
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
        }


class ImmunoprophylaxisInfForm(forms.ModelForm):
    class Meta:
        model = ImmunoprophylaxisInf
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'name': TinyMCE(),
        }



class ImmunoprophylaxisTipicalForm(forms.ModelForm):
    class Meta:
        model = ImmunoprophylaxisTipical
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'name_two': TinyMCE(),
            'name_three': TinyMCE(),
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'description_three': TinyMCE(),
        }


class ObjectivesForm(forms.ModelForm):
    class Meta:
        model = Objectives
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'name': TinyMCE(),
        }


class TicksForm(forms.ModelForm):
    class Meta:
        model = Ticks
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'name': TinyMCE(),
            'name_map': TinyMCE(),
        }


class StudiesForm(forms.ModelForm):
    class Meta:
        model = Studies
        fields = '__all__'
        widgets = {
            'desc': TinyMCE(),
            'indicators': TinyMCE(),
            'catering_workers': TinyMCE(),
            'name': TinyMCE(),
            'after_workers': TinyMCE(),
            'employees_school': TinyMCE(),
        }


class WaterQualitySafetyForm(forms.ModelForm):
    class Meta:
        model = WaterQualitySafety
        fields = '__all__'
        widgets = {
            'desc': TinyMCE(),
            'indicators': TinyMCE(),
            'mine_well': TinyMCE(),
            'name': TinyMCE(),
            'basic': TinyMCE(),
            'standart': TinyMCE(),
            'standart_plus': TinyMCE(),
        }


class LaboratoryFruitVegetableForm(forms.ModelForm):
    class Meta:
        model = LaboratoryFruitVegetable
        fields = '__all__'
        widgets = {
            'desc': TinyMCE(),
            'cost': TinyMCE(),
            'name': TinyMCE(),
            'paket': TinyMCE(),
        }


class EripPaymentForm(forms.ModelForm):
    class Meta:
        model = EripPayment
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'description_two': TinyMCE(),
            'payment_methods': TinyMCE(),
            'name': TinyMCE(),
            'unp': TinyMCE(),
            'title_portal': TinyMCE(),
        }


class PhotoDayForm(forms.ModelForm):
    class Meta:
        model = PhotoDay
        fields = '__all__'
        widgets = {
            'description': TinyMCE(),
            'name': TinyMCE(),
        }


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'adres': TinyMCE(),
            'mail': TinyMCE(),
            'phone': TinyMCE(),
        }


class CentreNewsForm(forms.ModelForm):
    class Meta:
        model = CentreNews
        fields = '__all__'
        widgets = {
            'name': TinyMCE(),
            'desc': TinyMCE(),
            'desc_hover': TinyMCE(),
            'author': TinyMCE(),
        }
