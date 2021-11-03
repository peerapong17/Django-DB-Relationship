from django.contrib import messages
from django.shortcuts import redirect, render

from football.models import Club, Continent, Country

# Create your views here.
def create(request):
    if request.method == "POST":
        name = request.POST['name']
        continent = request.POST['continent']
        country = request.POST['country']
        club = Club.objects.create(
            name=name, continent_id=continent, country_id=country)
        club.save()
        messages.success(request, "Create Club Success")
        return redirect("football_by_category", "Club")
        
    return render(request, 'club/create.html')

def club_by_Id(request, id):
    club = Club.objects.get(id=id)
    players = club.player_set.all()
    return render(request, 'club/index.html', {"players": players, "club": club})

def delete(request, id):
    club = Club.objects.get(id=id)
    club.delete()

    return redirect("football_by_category", "Club")

def update(request, id):
    club = Club.objects.get(id=id)
    if request.method == "POST":
        club.name = request.POST['name']
        club.continent_id = request.POST['continent']
        club.country_id = request.POST['country']
        club.save()
        messages.success(request, "Update Club Success")
        return redirect("football_by_category", "Continent")

    return render(request, 'club/update.html', {"club": club})