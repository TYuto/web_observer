from django.contrib import admin

# Register your models here.
from .models import Version, Site


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    pass

@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass