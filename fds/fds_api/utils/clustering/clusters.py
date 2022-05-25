from ..models import *
import pandas as pd

def player_grouping(player_id_list):
    players = Player.objects.filter(id__in = player_id_list).all()

    questions = Questions.objects.all()
    data = {}

