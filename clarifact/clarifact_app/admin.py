from django.contrib import admin
from .models import source

from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(source)

class sourceAdmin(ImportExportModelAdmin):
    pass