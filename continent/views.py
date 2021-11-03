from django.contrib import messages
from django.shortcuts import redirect, render
from football.models import Continent

# Create your views here.


def continent_by_Id(request, id):
    continent = Continent.objects.get(id=id)
    countries = continent.country_set.all()
    clubs = continent.club_set.all()
    return render(request, 'continent/index.html', {"countries": countries, "clubs": clubs, "continent": continent})


def create(request):
    if request.method == "POST":
        name = request.POST['continent']
        continent = Continent.objects.create(name=name)
        continent.save()
        messages.success(request, "Create Continent Success")
        return redirect("football_by_category", "Continent")

    return render(request, 'continent/create.html')

def delete(request, id):
    continent = Continent.objects.get(id=id)
    continent.delete()

    return redirect("football_by_category", "Continent")

def update(request, id):
    continent = Continent.objects.get(id=id)
    if request.method == "POST":
        continent.name = request.POST['continent']
        continent.save()
        messages.success(request, "Update Continent Success")
        return redirect("football_by_category", "Continent")

    return render(request, 'continent/update.html', {"continent": continent})
