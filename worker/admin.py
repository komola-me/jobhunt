from django.contrib import admin
from worker.models import WorkerProfile, Skill, Education, Experience, LanguageLevel, Address
from worker.models import Language, ProfessionalArea

# Register your models here.
class LanguageWithLevelInline(admin.TabularInline):
    model = LanguageLevel
    extra = 1


class AddressInline(admin.TabularInline):
    model = Address
    extra = 1


class ProfessionalArea(admin.TabularInline):
    model = ProfessionalArea
    extra = 1


class WorkerProfileAdmin(admin.ModelAdmin):
    inlines = [LanguageWithLevelInline, AddressInline, ProfessionalArea]


admin.site.register(WorkerProfile, WorkerProfileAdmin)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Language)

