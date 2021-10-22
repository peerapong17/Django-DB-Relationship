from django.db import models
from django.urls import reverse


class Continent(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_continent_by_Id(self):
        return reverse('continent_by_Id', args=[self.id])


class Country(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    continent = models.ForeignKey(Continent, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

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

    def get_club_by_Id(self):
        return reverse('club_by_Id', args=[self.id])


class Position(models.Model):

    position = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ['position']
    
    def get_position_by_Id(self):
        return reverse('position_by_Id', args=[self.id])


class Player(models.Model):

    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(blank=False, null=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    position = models.ManyToManyField(Position)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_player_by_Id(self):
        return reverse('player_by_Id', args=[self.id])
