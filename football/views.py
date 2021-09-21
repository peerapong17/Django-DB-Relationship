from django.shortcuts import render
from .models import Club, Continent, Country, Position, Player

types = ['Continent', 'Country', 'Club', 'Player']
createTypes = ['createCountry', "createClub", "createPlayer"]


def home(request):
    return render(request, 'home.html', {"types": types})


def football(request, search):
    datas = ''
    if search == "Continent":
        datas = Continent.objects.all()
    elif search == "Country":
        datas = Country.objects.all()
    elif search == "Club":
        datas = Club.objects.all()
    else:
        datas = Player.objects.all()

    return render(request, 'football.html', {"types": types, "datas": datas, "search": search, "createTypes": createTypes})


def continent(request, id):
    datas = Continent.objects.get(id=id)
    countries = datas.country_set.all()
    clubs = datas.club_set.all()
    return render(request, 'continent.html', {"types": types, "datas": datas, "countries": countries, "clubs": clubs})


def country(request, id):
    datas = Country.objects.get(id=id)
    clubs = datas.club_set.all()
    players = datas.player_set.all()
    return render(request, 'country.html', {"types": types, "datas": datas, "clubs": clubs, "players": players})


def club(request, id):
    datas = Club.objects.get(id=id)
    players = datas.player_set.all()
    return render(request, 'club.html', {"types": types, "datas": datas, "players": players})


def player(request, id):
    data = Player.objects.get(id=id)
    positions = data.position.all()
    return render(request, 'player.html', {"types": types, "data": data, "positions": positions})


def filteredByCountry(request, country):
    datas = Country.objects.get(name=country)
    clubs = datas.club_set.all()
    players = datas.player_set.all()
    return render(request, 'country.html', {"types": types, "datas": datas, "clubs": clubs, "players": players})


def filteredByClub(request, club):
    datas = Club.objects.get(name=club)
    players = datas.player_set.all()
    return render(request, 'club.html', {"types": types, "datas": datas, "players": players})


def position(request, position):
    datas = Position.objects.get(position=position)
    players = datas.player_set.all()
    return render(request, 'position.html', {"types": types, "datas": datas, "players": players, "position": position})


def createCountry(request):
    continents = Continent.objects.all()
    if request.method == "POST":
        continent = Continent.objects.get(id=request.POST['continent'])
        country = Country.objects.create(
            name=request.POST['country'], continent=continent)
        country.save()
    return render(request, 'createCountry.html', {"types": types, "createTypes": createTypes, "continents": continents})


def createClub(request):
    continents = Continent.objects.all()
    countries = Country.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        continent = Continent.objects.get(id=request.POST['continent'])
        country = Country.objects.get(id=request.POST['country'])
        club = Club.objects.create(
            name=name, continent=continent, country=country)
        club.save()
    return render(request, 'createClub.html', {"types": types, "createTypes": createTypes, "continents": continents, "countries": countries})


def createPlayer(request):
    clubs = Club.objects.all()
    countries = Country.objects.all()
    positions = Position.objects.all()
    if request.method == "POST":
        age = request.POST['age']
        name = request.POST['name']
        selectedPositions = request.POST.getlist('positions')
        club = Club.objects.get(id=request.POST['club'])
        country = Country.objects.get(id=request.POST['country'])
        player = Player.objects.create(
            name=name, age=age, club=club, country=country)
        for position in selectedPositions:
            relatedPosition = Position.objects.get(id=position)
            player.position.add(relatedPosition)

        player.save()
    return render(request, 'createPlayer.html', {"types": types, "createTypes": createTypes, "clubs": clubs, "countries": countries, "positions": positions})
