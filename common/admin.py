from django.contrib import admin
from common.models import User, Specialization, Category, District, Region

# Register your models here.
admin.site.register(User)
admin.site.register(Specialization)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Region)
