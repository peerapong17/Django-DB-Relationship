from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('football/', include('football.urls')),
    path('continent/', include('continent.urls')),
    path('country/', include('country.urls')),
    path('club/', include('club.urls')),
    path('player/', include('player.urls')),
    path('position/', include('position.urls')),
    path("", lambda request: redirect('football/', permanent=False)),
]
