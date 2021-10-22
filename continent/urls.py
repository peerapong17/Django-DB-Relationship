from django.contrib import admin
from django.urls import path, include
from continent import views

urlpatterns = [
    path('<int:id>', views.continent_by_Id, name="continent_by_Id")
]
