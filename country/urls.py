from django.contrib import admin
from django.urls import path, include
from country import views

urlpatterns = [
    path('create', views.create, name="create_country"),
    path('<int:id>', views.country_by_Id, name="country_by_Id"),
    path('delete/<int:id>', views.delete, name="delete_country"),
    path('update/<int:id>', views.update, name="update_country")
]
