from django.contrib import admin
from .models import Grave



class GraveAdmin(admin.ModelAdmin):
    list_display = ("FirstName", "LastName","Birth","Death")

admin.site.register(Grave, GraveAdmin)