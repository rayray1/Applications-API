from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListApps.as_view()),
]
