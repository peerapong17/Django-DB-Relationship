from django.contrib import admin
from django.urls import path, include
from player import views

urlpatterns = [
    path('create', views.create, name="create_player"),
    path('<int:id>', views.player_by_Id, name="player_by_Id"),
]
