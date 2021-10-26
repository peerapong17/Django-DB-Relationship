from football.models import Position, Continent, Country, Player, Club


def categories(request):
    categories = ['Continent', 'Country', 'Club', 'Player', 'Position']
    return dict(categories=categories)


def continents(request):
    continents = Continent.objects.all()
    return dict(continents=continents)


def countries(request):
    countries = Country.objects.all()
    return dict(countries=countries)


def clubs(request):
    clubs = Club.objects.all()
    return dict(clubs=clubs)


def players(request):
    players = Player.objects.all()
    return dict(players=players)


def positions(request):
    positions = Position.objects.all()
    return dict(positions=positions)
