from django.contrib import admin
from .models import Grave



class GraveAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "middle_name","birth","death")

admin.site.register(Grave, GraveAdmin)