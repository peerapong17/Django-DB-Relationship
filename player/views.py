from django.contrib import messages
from django.shortcuts import redirect, render

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
            positionNeeded = Position.objects.get(id=position)
            positionNeeded.player_set.add(player.id)

    return render(request, 'player/create.html')


def player_by_Id(request, id):
    player = Player.objects.get(id=id)
    positions = player.positions.all()
    return render(request, 'player/index.html', {"positions": positions, "player": player})


def delete(request, id):
    player = Player.objects.get(id=id)
    player.delete()

    return redirect("football_by_category", "Player")


def update(request, id):
    player = Player.objects.get(id=id)
    if request.method == "POST":
        player.age = request.POST['age']
        player.name = request.POST['name']
        player.club_id = request.POST['club']
        player.country_id = request.POST['country']
        playerPositionAll = player.positions.all()
        playerPositions = [position.id for position in playerPositionAll]
        checkboxPositions = request.POST.getlist('positions')
        selectedPositions = [int(position) for position in checkboxPositions]

        print(playerPositions)

        print(selectedPositions)

        for selectedPosition in selectedPositions:
            if selectedPosition in playerPositions:
                for playerPosition in playerPositions:
                    if playerPosition not in selectedPositions:
                        positionNeeded = Position.objects.get(
                            id=playerPosition)
                        positionNeeded.player_set.remove(player.id)
            else:
                positionNeeded = Position.objects.get(id=selectedPosition)
                positionNeeded.player_set.add(player.id)
                for playerPosition in playerPositions:
                    if playerPosition not in selectedPositions:
                        positionNeeded = Position.objects.get(
                            id=playerPosition)
                        positionNeeded.player_set.remove(player.id)

        # another way ##
        # for playerPosition in playerPositions:
        #     positionNeeded = Position.objects.get(id=playerPosition)
        #     positionNeeded.player_set.remove(player.id)
        #
        # for selectedPosition in selectedPositions:
        #     positionNeeded = Position.objects.get(id=selectedPosition)
        #     positionNeeded.player_set.add(player.id)

        player.save()
        messages.success(request, "Update Position Success")
        return redirect("football_by_category", "Player")

    return render(request, 'player/update.html', {"player": player})
