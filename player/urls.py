from django.contrib import admin
from django.urls import path
from player import views

urlpatterns = [
    path('create', views.create, name="create_player"),
    path('<int:id>', views.player_by_Id, name="player_by_Id"),
    path('delete/<int:id>', views.delete, name="delete_player"),
    path('update/<int:id>', views.update, name="update_player")
]
