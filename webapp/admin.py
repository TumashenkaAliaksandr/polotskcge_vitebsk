from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from .forms import AboutUsForm, ResearchesForm, LogoForm, FeaturedForm, ReceptionHoursForm, GeneralInfoForm


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
