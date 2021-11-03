from django.contrib import admin
from django.urls import path, include
from club import views

urlpatterns = [
    path('create', views.create, name="create_club"),
    path('<int:id>', views.club_by_Id, name="club_by_Id"),
    path('delete/<int:id>', views.delete, name="delete_club"),
    path('update/<int:id>', views.update, name="update_club")
]