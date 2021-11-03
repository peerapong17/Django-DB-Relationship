from django.contrib import messages
from django.shortcuts import redirect, render

from football.models import Country

# Create your views here.
def create(request):
    if request.method == "POST":
        continent = request.POST['continent']
        country = Country.objects.create(
            name=request.POST['country'], continent_id=continent)
        country.save()
        messages.success(request, "Create Country Success")
        return redirect("football_by_category", "Country")

    return render(request, 'country/create.html')

def country_by_Id(request, id):
    country = Country.objects.get(id=id)
    clubs = country.club_set.all()
    players = country.player_set.all()
    return render(request, 'country/index.html', {"clubs": clubs, "players": players, "country": country})

def delete(request, id):
    country = Country.objects.get(id=id)
    country.delete()

    return redirect("football_by_category", "Country")

def update(request, id):
    print(id)
    country = Country.objects.get(id=id)
    if request.method == "POST":
        country.name = request.POST['country']
        country.continent_id = request.POST['continent']
        country.save()
        messages.success(request, "Update Country Success")
        return redirect("football_by_category", "Country")

    return render(request, 'country/update.html', {"country": country})