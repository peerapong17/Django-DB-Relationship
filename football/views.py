from django.shortcuts import render
from .models import Club, Continent, Country, Position, Player

def home(request):
    return render(request, 'home/index.html')


def football_by_category(request, search):
    datas = ''
    if search == "Continent":
        datas = Continent.objects.all()
    elif search == "Country":
        datas = Country.objects.all()
    elif search == "Club":
        datas = Club.objects.all()
    elif search == "Position":
        datas = Position.objects.all()
    else:
        datas = Player.objects.all()

    return render(request, 'home/index.html', {"datas": datas, "search": search})

def player(request, id):
    data = Player.objects.get(id=id)
    positions = data.position.all()
    return render(request, 'player.html', {"data": data, "positions": positions})


def filteredByCountry(request, country):
    datas = Country.objects.get(name=country)
    clubs = datas.club_set.all()
    players = datas.player_set.all()
    return render(request, 'country.html', {"datas": datas, "clubs": clubs, "players": players})


def filteredByClub(request, club):
    datas = Club.objects.get(name=club)
    players = datas.player_set.all()
    return render(request, 'club.html', {"datas": datas, "players": players})


def position(request, position):
    datas = Position.objects.get(position=position)
    players = datas.player_set.all()
    return render(request, 'position.html', {"datas": datas, "players": players, "position": position})


