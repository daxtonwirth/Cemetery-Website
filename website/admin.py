from django.contrib import admin
from .models import Grave



class GraveAdmin(admin.ModelAdmin):
    list_display = ("Occupant","Birth","Death", "Grid")

admin.site.register(Grave, GraveAdmin)