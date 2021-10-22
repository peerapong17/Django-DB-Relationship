from django.shortcuts import render

from football.models import Continent, Country

# Create your views here.
def create(request):
    if request.method == "POST":
        continent = request.POST['continent']
        country = Country.objects.create(
            name=request.POST['country'], continent_id=continent)
        country.save()

    return render(request, 'country/create.html')

def country_by_Id(request, id):
    country = Country.objects.get(id=id)
    clubs = country.club_set.all()
    players = country.player_set.all()
    return render(request, 'country/index.html', {"clubs": clubs, "players": players, "country": country})