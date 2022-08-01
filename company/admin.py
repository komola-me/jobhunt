from django.contrib import admin
from company.models import CompanyProfile, Vacancy, CompanyAddress, WorkingField

# Register your models here.
class CompanyAddressInline(admin.TabularInline):
    model = CompanyAddress
    extra = 1


class CompanyOperatingField(admin.TabularInline):
    model = WorkingField
    extra = 1


class CompanyProfileAdmin(admin.ModelAdmin):
    inlines = [CompanyAddressInline, CompanyOperatingField]

admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(Vacancy)

