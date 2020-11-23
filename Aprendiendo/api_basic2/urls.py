from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.otrapagina),
    path('pagina1/', views.otrapagina2),
    path('pagina2/', views.otrapagina3),
]