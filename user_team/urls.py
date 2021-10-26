from django.contrib import admin
from django.urls import path
from user_team import views

urlpatterns = [
    path('', views.index, name="user_teams"),
    path('<int:team_id>/detail', views.team_detail, name="team_detail"),
    path('show_team_list/<int:player_id>', views.show_team_list, name="show_team_list"),
    path('add_to_team/<int:team_id>/<int:player_id>', views.add_to_team, name="add_to_team"),
    path('create', views.create, name="create_team"),
]
