from django.contrib import admin

from .models import Url

admin.site.site_header = "GetShourl Administration"

class UrlAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Url)