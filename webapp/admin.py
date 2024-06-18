from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from .forms import AboutUsForm, ResearchesForm, LogoForm, FeaturedForm, ReceptionHoursForm, GeneralInfoForm, \
    EducationalResourceAdminForm, ZojForm, Book_complaintForm, HotlineHoursForm, HotlineHours_TitleForm, \
    HotlineHours_Title_descForm, Electronic_appeals_Title_descForm, Organ_Title_descForm


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


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


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
