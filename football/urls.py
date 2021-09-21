from django.contrib import admin
from django.urls import path, include
from .views import home, football, continent, country, club, player, filteredByCountry, filteredByClub, position, createCountry, createClub, createPlayer

urlpatterns = [
    path('', home, name="home"),
    path('football/<str:search>', football, name="football"),
    path('football/Continent/<int:id>', continent, name="continent"),
    path('football/Country/<int:id>', country, name="country"),
    path('football/Country/<str:country>',
         filteredByCountry, name="filteredByCountry"),
    path('football/Club/<int:id>', club, name="club"),
    path('football/Club/name/<str:club>',
         filteredByClub, name="filteredByClub"),
    path('football/Player/<int:id>', player, name="player"),
    path('football/Position/<str:position>', position, name="position"),
    path('football/create/createCountry', createCountry, name="createCountry"),
    path('football/create/createClub', createClub, name="createClub"),
    path('football/create/createPlayer', createPlayer, name="createPlayer"),
]
