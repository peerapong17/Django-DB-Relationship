from django.contrib import messages
from django.shortcuts import redirect, render
from football.models import Position

# Create your views here.
def create(request):
    if request.method == "POST":
        position = request.POST['position']
        newPosition = Position.objects.create(name=position)
        newPosition.save()
        messages.success(request, "Update Continent Success")
        return redirect("football_by_category", "Position")

    return render(request, 'position/create.html')

def position_by_Id(request, id):
    position = Position.objects.get(id=id)
    players = position.player_set.all()
    return render(request, 'position/index.html', {"players": players, "position": position})

def delete(request, id):
    position = Position.objects.get(id=id)
    position.delete()

    return redirect("football_by_category", "Position")

def update(request, id):
    position = Position.objects.get(id=id)
    if request.method == "POST":
        position.name = request.POST['position']
        position.save()
        messages.success(request, "Update Position Success")
        return redirect("football_by_category", "Position")

    return render(request, 'position/update.html', {"position": position})
