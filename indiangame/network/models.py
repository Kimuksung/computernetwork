from django.db import models
from django.utils import timezone
# Create your models here.
class Player(models.Model):
    nickname = models.CharField(max_length = 20, null = False, unique = True)
    card = models.PositiveIntegerField(default = 0)
    prev_card = models.PositiveIntegerField(default = 0)
    chip = models.PositiveIntegerField(default = 0)
    bet = models.PositiveIntegerField(default = 0)
    is_joined = models.BooleanField(default = False, null = False)
    is_my_turn = models.BooleanField(default = False, null = False)
    is_show_result = models.PositiveIntegerField(default = 0)
    last_approach = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.nickname

class Room(models.Model):
    name = models.CharField(max_length = 40, null = False, unique = True)
    join_players = models.ManyToManyField(Player, null = True,blank=True)
    is_playing = models.BooleanField(default = False, null = False)
    current_player_number = models.PositiveIntegerField(default = 0, null = False)
    stack = models.PositiveIntegerField(default = 0, null = False)
    def __str__(self):
        return self.name
