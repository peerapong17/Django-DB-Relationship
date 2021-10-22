from django.contrib import admin
from django.urls import path, include
from football import views
urlpatterns = [
    path('', views.home, name="home"),
    path('<str:search>', views.football_by_category, name="football_by_category"),
    path('Country/<str:country>',
         views.filteredByCountry, name="filteredByCountry"),
    path('Club/name/<str:club>',
         views.filteredByClub, name="filteredByClub"),
    path('Position/<str:position>', views.position, name="position"),
]
