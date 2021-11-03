from django.contrib import admin
from django.urls import path
from position import views

urlpatterns = [
    path('create', views.create, name="create_position"),
    path('<int:id>', views.position_by_Id, name="position_by_Id"),
    path('delete/<int:id>', views.delete, name="delete_position"),
    path('update/<int:id>', views.update, name="update_position")
]
