from random import choices
from django.db import models
from django.utils.translation import gettext_lazy as _
from .accounts import *
from .event import *

from django.contrib.postgres.fields import HStoreField

class Skill(models.Model):

    class SkillWeight(models.IntegerChoices):
        NONE = 0
        VERY_LOW = 1
        LOW = 2
        MODERATE = 3
        HIGH = 4
        VERY_HIGH = 5

    club = models.ForeignKey('club', on_delete=models.CASCADE)
    name = models.CharField(_('Skill name'), max_length=100, blank=False)
    description = models.TextField(_("Skill Description"), blank=False)

    weight_for_GK = models.IntegerField(_("Level of importance for GKs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_DEF = models.IntegerField(_("Level of importance for DEFs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_MID = models.IntegerField(_("Level of importance for MIDs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_STR = models.IntegerField(_("Level of importance for GK"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)

class Parameters(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='parameters')
    skills = models.ManyToManyField(Skill, related_name='parameter', blank=True)

class Grade(models.Model):
    event = models.ForeignKey('event', on_delete=models.CASCADE, related_name='event_grades')
    scout = models.ForeignKey('scout', on_delete=models.DO_NOTHING, related_name='scouts_grade')
    player = models.ForeignKey('player',on_delete=models.DO_NOTHING, related_name='graded_players')
    score = models.JSONField(_("score"))
    aggregate = models.FloatField(_("Aggregate"), blank=False)

    def calculate_aggregate(self):
 
        weighted_sum = 0
        weights = []
        for s in self.score:
            skill = Skill.objects.filter(id = s).first()
            
            score = self.score[s]
            

            if 'GK' in self.player.more.playing_possition1:
                weighted_sum += skill.weight_for_GK * score
                weights.append(skill.weight_for_GK)

            elif 'DEF' in self.player.more.playing_possition1:
                weighted_sum += skill.weight_for_DEF * score
                weights.append(skill.weight_for_DEF)

            elif 'MID' in self.player.more.playing_possition1:
                weighted_sum += skill.weight_for_MID * score
                weights.append(skill.weight_for_MID)
                

            elif 'STR' in self.player.more.playing_possition1:
                weighted_sum += skill.weight_for_STR * score
                weights.append(skill.weight_for_STR)

        
        aggregate = weighted_sum / len(self.score)

        # convert out of 10
        maximum = 0
        for weight in weights:
            maximum += 10 * weight
        maximum = maximum / len(self.score)
        agg = 10*aggregate / maximum

        return agg