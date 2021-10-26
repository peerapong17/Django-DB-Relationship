from django.shortcuts import redirect, render
from football.models import UserTeam
from django.contrib import messages

# Create your views here.


def index(request):
    user_teams = UserTeam.objects.all()
    return render(request, 'user_team/index.html', {"user_teams": user_teams})


def team_detail(request, team_id):
    user_team = UserTeam.objects.get(id=team_id)
    players = user_team.players.all()
    return render(request, 'user_team/detail.html', {"user_team": user_team, "players": players})


def create(request):

    if request.method == "POST":
        name = request.POST['name']
        club = request.POST['club']

        UserTeam.objects.create(name=name, club_id=club)
        messages.success(request, "Create team success")
        return redirect(to="user_teams")

    return render(request, 'user_team/create.html')


def show_team_list(request, player_id):
    user_teams = UserTeam.objects.all()
    return render(request, 'user_team/show_team_list.html', {"user_teams": user_teams, "player_id": player_id})

def add_to_team(request, team_id ,player_id):
    user_team = UserTeam.objects.get(id=team_id)
    user_team.players.add(player_id)
    user_team.save()
    messages.success(request, "Player added")
    return redirect("team_detail", team_id)
