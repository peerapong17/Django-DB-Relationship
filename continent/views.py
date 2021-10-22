from django.shortcuts import render
from football.models import Continent

# Create your views here.
def continent_by_Id(request, id):
    continent = Continent.objects.get(id=id)
    countries = continent.country_set.all()
    clubs = continent.club_set.all()
    return render(request, 'continent/index.html', {"countries": countries, "clubs": clubs, "continent": continent})
