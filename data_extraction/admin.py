from django.contrib import admin
from .models import *

# Company.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "company_name")
admin.site.register(Company, CompanyAdmin)

# CompanyNameCorrections
class CompanyNameCorrectionsAdmin(admin.ModelAdmin):
    list_display = ("id", "alternateName", "correctName")
    list_filter = ("correctName",)
admin.site.register(CompanyNameCorrections, CompanyNameCorrectionsAdmin)

# Data. 
class DataAdmin(admin.ModelAdmin):
    list_display = ("id", "page")
admin.site.register(Data, DataAdmin)

# Document. 
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "well", "document_name", "report", "status", "url")
    list_filter = ("report__report_type", "well", "document_name", "status")
admin.site.register(Document, DocumentAdmin)

# Report. 
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "well", "report_type", "report_name", "gov_report_name", "gov_id", "url")
    list_filter = ("well", "report_type")
admin.site.register(Report, ReportAdmin)

# Report Type.
admin.site.register(ReportType)

# File. 
class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "file_name", "file_ext", "file_location")
admin.site.register(File, FileAdmin)

# Page. 
class PageAdmin(admin.ModelAdmin):
    list_display = ("id", "document", "page_no", "file")
admin.site.register(Page, PageAdmin)

# Text
admin.site.register(Text)

# BoundingPoly
admin.site.register(BoundingPoly)

# Permit.
admin.site.register(Permit)

# State.
class StateAdmin(admin.ModelAdmin):
    list_display = ("name_short", "name_long")
admin.site.register(State, StateAdmin)

# WellStatus.
admin.site.register(WellStatus)

# Well Class. 
admin.site.register(WellClass)

# Well Purpose. 
admin.site.register(WellPurpose)

# Well.
class WellAdmin(admin.ModelAdmin):
    list_display = ("id", "well_name", "owner", "state","permit", "status", "well_class", "purpose")
    list_filter = ("well_name", "owner", "state", "permit", "status", "well_class", "purpose")
admin.site.register(Well, WellAdmin)

# UserProfiles
admin.site.register(UserProfile)

# Organisation
admin.site.register(Organisation)



# Data Extraction
class ExtractionActionsInline(admin.TabularInline):
    model = ExtractionActions
    extra=1
    verbose_name = "Action"
    verbose_name_plural = "Actions"
    show_change_link = True

class ExtractionMethodAdmin(admin.ModelAdmin):
    list_display = ['id','data_type','company','name']
    search_fields = ['name']
    inlines = [ExtractionActionsInline]
    def get_ordering(self, request):
        return ['data_type', 'id']
admin.site.register(ExtractionMethod, ExtractionMethodAdmin)

class ExtractionActionsAdmin(admin.ModelAdmin):
    list_display = ['id','method','order','action']
    search_fields = ['name']
    def get_ordering(self, request):
        return ['method', 'order']
admin.site.register(ExtractionActions, ExtractionActionsAdmin)