from django.shortcuts import render
from football.models import Position

# Create your views here.
def position_by_Id(request, id):
    position = Position.objects.get(id=id)
    players = position.player_set.all()
    return render(request, 'position/index.html', {"players": players, "position": position})