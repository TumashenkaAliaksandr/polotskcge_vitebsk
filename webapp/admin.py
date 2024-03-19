from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position', 'phone', 'department', 'appointment_time']
    search_fields = ['first_name', 'last_name', 'position', 'phone', 'department', 'appointment_time']
    list_filter = ['department']

admin.site.register(Doctor, DoctorAdmin)