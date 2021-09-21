from django.contrib import admin
from .models import Continent, Club, Country, Player, Position

# Register your models here.
admin.site.register(Continent)
admin.site.register(Club)
admin.site.register(Country)
admin.site.register(Player)
admin.site.register(Position)