from django.db import models
from django.utils.translation import gettext_lazy as _

from .accounts import *



class Event(models.Model):

    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"

    class RequiredPossition(models.TextChoices):
        GK = "goalkeepers"
        DEF = "defenders"
        MID = "midfielders"
        STR = "strikers"
        ANY = "any"
        

    club = models.ForeignKey("club", on_delete=models.DO_NOTHING, related_name='events')
    posted_date = models.DateField(auto_now=True)
    starting_date = models.DateField(_("Event start date"), auto_now=False, auto_now_add=False, blank=False)
    application_deadline = models.DateField(_("Application Deadline"), auto_now=False, auto_now_add=False, blank=False)
    description = models.TextField(_("Description"))

    required_positions = models.CharField(_('Required positions'), max_length=50, choices=RequiredPossition.choices, blank=False) #multi options problem!!!!!

    age_limit = models.IntegerField(_("Age limit"), blank=False)
    education_level = models.CharField(_("Education level"), max_length=200)
    location = models.CharField(_("Location"),blank=False, max_length=200)
    gender = models.CharField(_("Gender"), max_length=50, choices=Gender.choices, blank=False)
    session_time_for_each = models.IntegerField(_("Session time"), blank=False)
    
    applicants = models.ManyToManyField(Player, related_name='applicants', blank=True)
    candidates = models.ManyToManyField(Player, related_name='candidates', blank=True)
    accepted_applicants = models.ManyToManyField(Player, related_name='accepted_applicants', blank=True)

    scouts = models.ManyToManyField(Scout, related_name='assigned_eventd', blank=True)

    # parameters = models.OneToOneField('parameters', on_delete=models.CASCADE)


