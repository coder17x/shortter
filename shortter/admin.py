from django.contrib import admin

from .models import Links


class LinksAdmin(admin.ModelAdmin):
    list_display = ("lnk_id", "lnk_short_name", "lnk_full_name",)


admin.site.register(Links, LinksAdmin)
