from django.urls import path, include
from . import views

urlpatterns = [
    path('cron_task/', views.cronTask),
    path('version/<str:version>/', views.versionView),
    path('diff/<str:past>/<str:current>', views.diffView),
    path('latest/<str:siteid>', views.latestView),
\
]