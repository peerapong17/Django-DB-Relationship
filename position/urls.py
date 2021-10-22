from django.contrib import admin
from django.urls import path
from position import views

urlpatterns = [
    path('<int:id>', views.position_by_Id, name="position_by_Id"),
]
