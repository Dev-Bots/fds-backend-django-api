from django.db import models
from django.utils.translation import gettext_lazy as _
from .accounts import *
from .event import *


class Team(models.Model):

    players = models.ManyToManyField(Player, blank=True)
    formation = models.CharField(_("Formation"), max_length=255, blank=False)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, related_name='teams')

class Match(models.Model):

    team1 = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name='team2')
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, related_name='matches')







