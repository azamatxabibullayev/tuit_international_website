from django.contrib import admin
from .models import Program, Application

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "program", "submitted_at")
