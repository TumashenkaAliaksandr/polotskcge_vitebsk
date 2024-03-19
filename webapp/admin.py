from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from .models import *

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
