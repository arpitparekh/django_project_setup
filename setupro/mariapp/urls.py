from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('intro/',views.showIntroPage, name='intro'),
]
