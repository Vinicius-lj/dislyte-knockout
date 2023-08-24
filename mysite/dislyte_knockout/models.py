from django.db import models

class Esper(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    classe = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50)
    leader_effect = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    server = models.CharField(max_length=50)
    guild = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Player_esper(models.Model):
    ressonance = models.IntegerField(default=0)
    team = models.IntegerField(default=1)
    ifleader = models.BooleanField(default=False)
    version = models.CharField(max_length=15, default=0)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    esper_id = models.ForeignKey(Esper, on_delete=models.CASCADE)
