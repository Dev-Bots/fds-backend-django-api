
from django.db import models
from django.utils.translation import gettext_lazy as _
from .accounts import *



class Question(models.Model):
    question = models.TextField(_("Question"), blank=False)
    
    
class Choice(models.Model):
    title = models.TextField(_("Choice"), blank=False)
    question = models.ForeignKey("question", verbose_name=_("Question"), on_delete=models.CASCADE, related_name="choices")


class Answer(models.Model):
    player_id = models.ForeignKey("account", verbose_name=_("Player"), on_delete=models.DO_NOTHING)
    question = models.ForeignKey("question", verbose_name=_("Question"), on_delete=models.DO_NOTHING)
    answer = models.CharField(_("Answer"), max_length=255, blank=False)