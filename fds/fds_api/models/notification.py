from django.db import models
from django.utils.translation import gettext_lazy as _

from .accounts import *

class Notification(models.Model):
    to = models.OneToOneField(Account, related_name="notified_account", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250, blank=False)
    content = models.TextField(_("Notification content"), blank=False)
    date = models.DateField(_("Notified date"), auto_now=True)
