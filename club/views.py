from django.shortcuts import render

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
    return render(request, 'club/create.html')

def club_by_Id(request, id):
    club = Club.objects.get(id=id)
    players = club.player_set.all()
    return render(request, 'club/index.html', {"players": players, "club": club})