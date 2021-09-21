from django.db import models


class Continent(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Country(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    continent = models.ForeignKey(Continent, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Club(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    continent = models.ForeignKey(
        Continent, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Position(models.Model):

    position = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ['position']


class Player(models.Model):

    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(blank=False, null=False)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True)
    position = models.ManyToManyField(Position)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
