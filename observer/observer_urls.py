from django.urls import path, include
from . import views

urlpatterns = [
    path('cron_task/', views.cronTask)
]