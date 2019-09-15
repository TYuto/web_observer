from django.contrib import admin

# Register your models here.
from .models import Version, Site


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass