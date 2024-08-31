from tinymce.widgets import TinyMCE
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags
from .forms import *


class DoctorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name', 'last_name', 'position', 'phone', 'department', 'appointment_time']
    search_fields = ['first_name', 'last_name', 'position', 'phone', 'department', 'appointment_time']
    list_filter = ['department']


admin.site.register(Doctor, DoctorAdmin)


class Services_titleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ['name', 'description']
    list_filter = ['name']


admin.site.register(Services_title, Services_titleAdmin)


class ServicesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ['name', 'description']
    list_filter = ['name']


admin.site.register(Services, ServicesAdmin)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке


@admin.register(Laboratory)
class LabaAdmin(admin.ModelAdmin):
    form = LabaForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке


@admin.register(Laboratories)
class LaboratoriesAdmin(admin.ModelAdmin):
    form = LaboratoriesForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке


@admin.register(Zoj)
class ZojUsAdmin(admin.ModelAdmin):
    form = ZojForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке


@admin.register(Researches)
class ResearchesAdmin(admin.ModelAdmin):
    form = ResearchesForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name', 'name_two', 'name_three', 'name_four', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    form = LogoForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    form = FeaturedForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    form = ApRegistrationForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    form = RelationForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(HumanResourcesDesc)
class HumanResourcesDescAdmin(admin.ModelAdmin):
    form = HumanResourcesDescForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(HumanResources)
class HumanResourcesAdmin(admin.ModelAdmin):
    form = HumanResourcesForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Accounting)
class AccountingAdmin(admin.ModelAdmin):
    form = AccountingForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(AccountingDesc)
class AccountingDescAdmin(admin.ModelAdmin):
    form = AccountingDescForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Book_complaint)
class Book_complaintAdmin(admin.ModelAdmin):
    form = Book_complaintForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(UnionDesc)
class UnionDescAdmin(admin.ModelAdmin):
    form = UnionDescForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ListingDecree)
class ListingDecreeAdmin(admin.ModelAdmin):
    form = ListingDecreeForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ListingDecreeDesc)
class ListingDecreeDescAdmin(admin.ModelAdmin):
    form = ListingDecreeDescForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Union)
class UnionAdmin(admin.ModelAdmin):
    form = UnionForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Profsouz)
class ProfsouzAdmin(admin.ModelAdmin):
    form = ProfsouzForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ProfsouzTwo)
class ProfsouzTwoAdmin(admin.ModelAdmin):
    form = ProfsouzTwoForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ProfsouzDescOne)
class ProfsouzDescOneAdmin(admin.ModelAdmin):
    form = ProfsouzDescOneForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ProfsouzIcons)
class ProfsouzIconsAdmin(admin.ModelAdmin):
    form = ProfsouzIconsForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


class ProfsouzDescAdmin(admin.ModelAdmin):
    form = ProfsouzDescForm

    def get_changeform_initial_data(self, request):
        return {"name": "custom_initial_value"}


admin.site.register(ProfsouzDesc, ProfsouzDescAdmin)


@admin.register(ReceptionHours)
class ReceptionHoursAdmin(admin.ModelAdmin):
    form = ReceptionHoursForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    form = GeneralInfoForm
    list_display = ['title']

    def description_preview(self, obj):
        return obj.description[:50]  # Предположим, что вы хотите отображать только первые 50 символов описания

    description_preview.short_description = 'Описание'


class HotlineHoursAdmin(admin.ModelAdmin):
    form = HotlineHoursForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    list_filter = ('date_hotline',)


admin.site.register(HotlineHours, HotlineHoursAdmin)


class HotlineHours_TitleAdmin(admin.ModelAdmin):
    form = HotlineHours_TitleForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'description')


admin.site.register(HotlineHours_Title, HotlineHours_TitleAdmin)


class HotlineHours_Title_descAdmin(admin.ModelAdmin):
    form = HotlineHours_Title_descForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'description')


admin.site.register(HotlineHours_Title_desc, HotlineHours_Title_descAdmin)


class Electronic_appeals_Title_descAdmin(admin.ModelAdmin):
    form = Electronic_appeals_Title_descForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'description')


admin.site.register(Electronic_appeals_Title_desc, Electronic_appeals_Title_descAdmin)


class Organ_Title_descAdmin(admin.ModelAdmin):
    form = Organ_Title_descForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'description')


admin.site.register(Organ_Title_desc, Organ_Title_descAdmin)


class Up_Organ_inf_Admin(admin.ModelAdmin):
    form = Up_Organ_infForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'description')


admin.site.register(Up_Organ_inf, Up_Organ_inf_Admin)


class Up_OrganAdmin(admin.ModelAdmin):
    form = Up_Organ_Form

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


admin.site.register(Up_Organ, Up_OrganAdmin)


class NormativeDocumentsAdmin(admin.ModelAdmin):
    form = NormativeDocuments_Form

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


admin.site.register(NormativeDocuments, NormativeDocumentsAdmin)


class ExpertiseAdmin(admin.ModelAdmin):
    form = Expertise_Form

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'description', 'description_two', 'description_three')


admin.site.register(Expertise, ExpertiseAdmin)


class DutiesAdmin(admin.ModelAdmin):
    form = Duties_Form

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'description')


admin.site.register(Duties, DutiesAdmin)


class MaintenanceShAdmin(admin.ModelAdmin):
    form = MaintenanceSh_Form

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'description')


admin.site.register(MaintenanceSchedule, MaintenanceShAdmin)


class VacanciesAdmin(admin.ModelAdmin):
    form = Vacancies_Form

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'vacancy')


admin.site.register(Vacancies, VacanciesAdmin)


class AppealsAdmin(admin.ModelAdmin):
    form = Appeals_Form

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name', 'name_two', 'name_three', 'appeals_desc', 'appeals_desc_two', 'appeals_desc_three', 'appeals_desc_four')


admin.site.register(MainAppeals, AppealsAdmin)


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class AnticorrTitleAdmin(admin.ModelAdmin):
    form = AnticorrTitleForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    list_filter = ('name',)
    search_fields = ('name', 'desc_anticorr')


admin.site.register(AnticorrTitle, AnticorrTitleAdmin)


class AnticorrAdmin(admin.ModelAdmin):
    form = AnticorrForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    list_filter = ('name',)
    search_fields = ('name', 'description')


admin.site.register(Anticorr, AnticorrAdmin)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)


@admin.register(Question_Ansver_title)
class Question_Ansver_titleAdmin(admin.ModelAdmin):

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    search_fields = ('name',)
    list_per_page = 20


class EducationalResourceAdmin(admin.ModelAdmin):
    form = EducationalResourceAdminForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    list_filter = ('pub_date',)
    search_fields = ('name', 'description')
    ordering = ['-pub_date']

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'pdf_file', 'icon_class', 'pub_date')
        }),
    )


admin.site.register(EducationalResource, EducationalResourceAdmin)


class InformationAnalyticalAdmin(admin.ModelAdmin):
    form = InformationAnalyticalForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
    list_filter = ('pub_date',)
    search_fields = ('name', )
    ordering = ['-pub_date']

    fieldsets = (
        (None, {
            'fields': ('name', 'pdf_file', 'icon_class', 'pub_date')
        }),
    )


admin.site.register(InformationAnalytical, InformationAnalyticalAdmin)


@admin.register(Disinfection)
class DisinfectionAdmin(admin.ModelAdmin):
    form = DisinfectionForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Deratization)
class DeratizationAdmin(admin.ModelAdmin):
    form = DeratizationForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Disinsection)
class DeratizationAdmin(admin.ModelAdmin):
    form = DisinsectionForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(DisinfectionDesc)
class DeratizationAdmin(admin.ModelAdmin):
    form = DisinfectionDescForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    form = InventoryForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ControlNadzorTipical)
class ControlNadzorAdmin(admin.ModelAdmin):
    form = ControlNadzorTipicalForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(CNadTipicalName)
class CNadTipicalNameAdmin(admin.ModelAdmin):
    form = CNadTipicalNameForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(CustomProductsInf)
class CustomProductsInfAdmin(admin.ModelAdmin):
    form = CustomProductsInfForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(CustomProductsName)
class CustomProductsNameAdmin(admin.ModelAdmin):
    form = CustomProductsNameForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(EpidemialogyName)
class EpidemialogyNameAdmin(admin.ModelAdmin):
    form = EpidemialogyNameForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(EpidemialogyTipical)
class EpidemialogyNameAdmin(admin.ModelAdmin):
    form = EpidemialogyTipicalForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']



@admin.register(ServicesLawyerName)
class ServicesLawyerNameAdmin(admin.ModelAdmin):
    form = ServicesLawyerNameForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ServicesLawyerTipical)
class ServicesLawyerTipicalNameAdmin(admin.ModelAdmin):
    form = ServicesLawyerTipicalForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ImmunoprophylaxisInf)
class ImmunoprophylaxisInfAdmin(admin.ModelAdmin):
    form = ImmunoprophylaxisInfForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ImmunoprophylaxisTipical)
class ImmunoprophylaxisTipicalAdmin(admin.ModelAdmin):
    form = ImmunoprophylaxisTipicalForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(ImmunoprophylaxisName)
class ImmunoprophylaxisTipicalAdmin(admin.ModelAdmin):
    form = ImmunoprophylaxisNameForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(EconimicSouz)
class EconimicSouzAdmin(admin.ModelAdmin):
    form = EconimicSouz_Form

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Quarantine)
class QuarantineAdmin(admin.ModelAdmin):
    form = QuarantineForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(EpidemSituations)
class EpidemSituationsAdmin(admin.ModelAdmin):
    form = EpidemialSituationsForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']

@admin.register(CountryRegistry)
class CountryRegistryAdmin(admin.ModelAdmin):
    form = CountryRegistryForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Healthy)
class HealthyAdmin(admin.ModelAdmin):
    form = HealthyForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(HealthyTitle)
class HealthyTitleAdmin(admin.ModelAdmin):
    form = HealthyTitleForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Resolution)
class ResolutionAdmin(admin.ModelAdmin):
    form = ResolutionForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Objectives)
class ObjectivesAdmin(admin.ModelAdmin):
    form = ObjectivesForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'name'
    list_display = ['clean_name']


@admin.register(Ticks)
class TicksAdmin(admin.ModelAdmin):
    form = TicksForm

    # Кастомное поле для отображения очищенного текста
    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'name'
    list_display = ['clean_name']


@admin.register(ContactInfoHad)
class ContactInfoHadAdmin(admin.ModelAdmin):
    form = ContactInfoHadForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Studies)
class StudiesAdmin(admin.ModelAdmin):
    form = StudiesForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(WaterQualitySafety)
class WaterQualitySafetyAdmin(admin.ModelAdmin):
    form = WaterQualitySafetyForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(LaboratoryFruitVegetable)
class LaboratoryFruitVegetableAdmin(admin.ModelAdmin):
    form = LaboratoryFruitVegetableForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(EripPayment)
class EripPayAdmin(admin.ModelAdmin):
    form = EripPaymentForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(PhotoDay)
class PhotoDayAdmin(admin.ModelAdmin):
    form = PhotoDayForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    form = ContactsForm

    def clean_name(self, obj):
        return strip_tags(obj.name)

    clean_name.short_description = 'Name'
    list_display = ['clean_name']
