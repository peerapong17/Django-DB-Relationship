from django.shortcuts import render

from football.models import Player, Position

# Create your views here.


def create(request):
    if request.method == "POST":
        age = request.POST['age']
        name = request.POST['name']
        selectedPositions = request.POST.getlist('positions')
        club = request.POST['club']
        country = request.POST['country']
        player = Player.objects.create(
            name=name, age=age, club_id=club, country_id=country)
        player.save()

        for position in selectedPositions:
            # relatedPosition = Position.objects.get(id=position)
            # player.position.add(relatedPosition.id)
            positionneeded = Position.objects.get(id=position)
            positionneeded.player_set.add(player.id)

    return render(request, 'player/create.html')


def player_by_Id(request, id):
    player = Player.objects.get(id=id)
    positions = player.position.all()
    return render(request, 'player/index.html', {"positions": positions, "player": player})
