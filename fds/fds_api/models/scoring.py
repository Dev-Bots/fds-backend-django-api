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

    