from django.contrib import admin

from .models import Url

class UrlAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Url)