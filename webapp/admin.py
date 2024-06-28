from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from .forms import AboutUsForm, ResearchesForm, LogoForm, FeaturedForm, ReceptionHoursForm, GeneralInfoForm, \
    EducationalResourceAdminForm, ZojForm, Book_complaintForm, HotlineHoursForm, HotlineHours_TitleForm, \
    HotlineHours_Title_descForm, Electronic_appeals_Title_descForm, Organ_Title_descForm, Up_Organ_Form, \
    Up_Organ_infForm, Expertise_Form, Duties_Form, MaintenanceSh_Form, Vacancies_Form, Appeals_Form, AnticorrForm, \
    AnticorrTitleForm, NormativeDocuments_Form, LabaForm


class DoctorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    list_display = ['first_name', 'last_name', 'position', 'phone', 'department', 'appointment_time']
    search_fields = ['first_name', 'last_name', 'position', 'phone', 'department', 'appointment_time']
    list_filter = ['department']


admin.site.register(Doctor, DoctorAdmin)


class Services_titleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['name']


admin.site.register(Services_title, Services_titleAdmin)


class ServicesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    list_display = ['name', 'description', 'link']
    search_fields = ['name', 'description']
    list_filter = ['name']


admin.site.register(Services, ServicesAdmin)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsForm
    list_display = ['name', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке

@admin.register(Laboratory)
class LabaAdmin(admin.ModelAdmin):
    form = LabaForm
    list_display = ['name', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке

@admin.register(Zoj)
class ZojUsAdmin(admin.ModelAdmin):
    form = ZojForm
    list_display = ['name', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке


@admin.register(Researches)
class ResearchesAdmin(admin.ModelAdmin):
    form = ResearchesForm
    list_display = ['name', 'name_two', 'name_three', 'name_four', 'photo_display']  # Добавляем поле для отображения фотографии в списке

    def photo_display(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="100">')
        else:
            return "No photo"

    photo_display.short_description = 'Photo'  # Заголовок колонки в списке


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    form = LogoForm

@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    form = FeaturedForm

@admin.register(Book_complaint)
class Book_complaintAdmin(admin.ModelAdmin):
    form = Book_complaintForm

@admin.register(ReceptionHours)
class ReceptionHoursAdmin(admin.ModelAdmin):
    form = ReceptionHoursForm
    list_display = ['name', 'last_name', 'family_name', 'office', 'phone', 'reception_time']

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    form = GeneralInfoForm
    list_display = ['title', 'description']

    def description_preview(self, obj):
        return obj.description[:50]  # Предположим, что вы хотите отображать только первые 50 символов описания

    description_preview.short_description = 'Описание'

class HotlineHoursAdmin(admin.ModelAdmin):
    form = HotlineHoursForm
    list_display = ('name', 'post', 'phone', 'reception_time', 'date_hotline')
    list_filter = ('date_hotline',)

admin.site.register(HotlineHours, HotlineHoursAdmin)


class HotlineHours_TitleAdmin(admin.ModelAdmin):
    form = HotlineHours_TitleForm
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(HotlineHours_Title, HotlineHours_TitleAdmin)


class HotlineHours_Title_descAdmin(admin.ModelAdmin):
    form = HotlineHours_Title_descForm
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(HotlineHours_Title_desc, HotlineHours_Title_descAdmin)



class Electronic_appeals_Title_descAdmin(admin.ModelAdmin):
    form = Electronic_appeals_Title_descForm
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Electronic_appeals_Title_desc, Electronic_appeals_Title_descAdmin)


class Organ_Title_descAdmin(admin.ModelAdmin):
    form = Organ_Title_descForm
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Organ_Title_desc, Organ_Title_descAdmin)


class Up_Organ_inf_Admin(admin.ModelAdmin):
    form = Up_Organ_infForm
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Up_Organ_inf, Up_Organ_inf_Admin)


class Up_OrganAdmin(admin.ModelAdmin):
    form = Up_Organ_Form
    list_display = ('name', 'post', 'phone', 'reception_time')

admin.site.register(Up_Organ, Up_OrganAdmin)


class NormativeDocumentsAdmin(admin.ModelAdmin):
    form = NormativeDocuments_Form
    list_display = ('name', 'normative_desc')

admin.site.register(NormativeDocuments, NormativeDocumentsAdmin)


class ExpertiseAdmin(admin.ModelAdmin):
    form = Expertise_Form
    list_display = ('name', 'description', 'description_two', 'description_three')
    search_fields = ('name', 'description', 'description_two', 'description_three')


admin.site.register(Expertise, ExpertiseAdmin)


class DutiesAdmin(admin.ModelAdmin):
    form = Duties_Form
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Duties, DutiesAdmin)


class MaintenanceShAdmin(admin.ModelAdmin):
    form = MaintenanceSh_Form
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(MaintenanceSchedule, MaintenanceShAdmin)

class VacanciesAdmin(admin.ModelAdmin):
    form = Vacancies_Form
    list_display = ('name', 'vacancy', 'vacancy_two', 'vacancy_three')
    search_fields = ('name', 'vacancy', 'vacancy_two', 'vacancy_three')


admin.site.register(Vacancies, VacanciesAdmin)


class AppealsAdmin(admin.ModelAdmin):
    form = Appeals_Form
    list_display = ('name', 'name_two', 'name_three', 'appeals_desc', 'appeals_desc_two', 'appeals_desc_three', 'appeals_desc_four')
    search_fields = ('name', 'name_two', 'name_three', 'appeals_desc', 'appeals_desc_two', 'appeals_desc_three', 'appeals_desc_four')


admin.site.register(MainAppeals, AppealsAdmin)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class AnticorrTitleAdmin(admin.ModelAdmin):
    form = AnticorrTitleForm
    list_display = ('name', 'desc_anticorr')
    list_filter = ('name',)
    search_fields = ('name', 'desc_anticorr')

admin.site.register(AnticorrTitle, AnticorrTitleAdmin)


class AnticorrAdmin(admin.ModelAdmin):
    form = AnticorrForm
    list_display = ('name', 'description', 'link', 'icon_class')
    list_filter = ('name',)
    search_fields = ('name', 'description')

admin.site.register(Anticorr, AnticorrAdmin)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)


@admin.register(Question_Ansver_title)
class Question_Ansver_titleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_per_page = 20


class EducationalResourceAdmin(admin.ModelAdmin):
    form = EducationalResourceAdminForm
    list_display = ('name', 'pub_date', 'pdf_file', 'icon_class')
    list_filter = ('pub_date',)
    search_fields = ('name', 'description')
    ordering = ['-pub_date']

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'pdf_file', 'icon_class', 'pub_date')
        }),
    )

admin.site.register(EducationalResource, EducationalResourceAdmin)
