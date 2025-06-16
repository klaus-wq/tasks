from django.db import models

class Island(models.Model):
    name = models.CharField(max_length=200)

    def can_reach(self, island, *, by_ship):
        return by_ship in self.ships.all() and by_ship in island.ships.all()

class Ship(models.Model):
    name = models.CharField(max_length=200)
    islands = models.ManyToManyField(Island, related_name='ships')
