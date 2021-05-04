from django.contrib import admin

from .models import Ipo, SecurityCompany

@admin.register(Ipo)
class IpoAdmin(admin.ModelAdmin):
    pass

@admin.register(SecurityCompany)
class SecurityCompanyAdmin(admin.ModelAdmin):
    pass