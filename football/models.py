from django.db import models
from django.urls import reverse


class Continent(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = ("continents")

    def get_continent_by_Id(self):
        return reverse('continent_by_Id', args=[self.id])


class Country(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    continent = models.ForeignKey(Continent, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = ("countries")

    def get_country_by_Id(self):
        return reverse('country_by_Id', args=[self.id])


class Club(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    continent = models.ForeignKey(
        Continent, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = ("clubs")

    def get_club_by_Id(self):
        return reverse('club_by_Id', args=[self.id])


class Position(models.Model):

    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        db_table = ("positions")
    
    def get_position_by_Id(self):
        return reverse('position_by_Id', args=[self.id])


class Player(models.Model):

    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(blank=False, null=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    positions = models.ManyToManyField(Position)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = ("players")

    def get_player_by_Id(self):
        return reverse('player_by_Id', args=[self.id])

class UserTeam(models.Model):

    name = models.CharField(max_length=50, null=False)
    players = models.ManyToManyField(Player)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        db_table = ("user_teams")

    def get_detail(self):
        return reverse('team_detail', args=[self.id])
