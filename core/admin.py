from django.contrib import admin

from .models import Url

admin.site.site_header = "GetShourl Administration"

class UrlAdmin(admin.ModelAdmin):
    list_display = ['url', 'redirect_url', 'total_clicks', 'add_tm']

admin.site.register(Url, UrlAdmin)