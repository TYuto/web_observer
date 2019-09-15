from django.shortcuts import render
from django.http import HttpResponse

from .models import Site, Version
from . import scraper

def versionView(request, version):
    v = Version.objects.filter(id=version).first()
    return render(request, 'observer/version.html', {'v': v, 'updated_at': v.updated_at.strftime('%Y/%m/%d %H:%M') })

def diffView(request, past, current):
    v1 = Version.objects.filter(id=past).first()
    v2 = Version.objects.filter(id=current).first()
    v1updated = v1.updated_at.strftime('%Y/%m/%d %H:%M') 
    v2created = v2.created_at.strftime('%Y/%m/%d %H:%M') 
    return render(request, 'observer/diff.html', { "v1": v1, "v2": v2, "v1updated": v1updated, "v2created": v2created })
def latestView(request, siteid):
    v = Version.objects.filter(site=siteid).order_by('-updated_at').first()
    return render(request, 'observer/latest.html', { "v": v})

def cronTask(requests):
    for site in Site.objects.all():
        html = eval("scraper." + site.key)(site)
        current_version = Version.objects.filter(site=site).order_by('-updated_at').first()
        if current_version.html == html:
            current_version.save()
        else:
            Version.objects.create(html=html, site=site).save()
    return HttpResponse("ok")

