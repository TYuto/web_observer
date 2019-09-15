from django.shortcuts import render
from django.http import HttpResponse

from .models import Site, Version
from . import scraper

def cronTask(requests):
    for site in Site.objects.all():
        html = eval("scraper." + site.key)(site)
        current_version = Version.objects.filter(site=site).order_by('-updated_at').first()
        if current_version.html == html:
            current_version.save()
        else:
            Version.objects.create(html=html, site=site).save()
    return HttpResponse("ok")
