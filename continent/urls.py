from django.contrib import admin
from django.urls import path, include
from continent import views

urlpatterns = [
    path('create', views.create, name="create_continent"),
    path('<int:id>', views.continent_by_Id, name="continent_by_Id"),
    path('delete/<int:id>', views.delete, name="delete_continent"),
    path('update/<int:id>', views.update, name="update_continent")
]
