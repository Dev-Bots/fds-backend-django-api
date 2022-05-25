from ...models import *
import random

def classify_possition(players):

    classified = {}

    player_more = PlayerMore.objects.filter(playing_possition1 = 'GK').all()
    GK = players.filter(id__in = [ player.id for player in player_more]).all()

    player_more = PlayerMore.objects.filter(playing_possition1 = 'DEF').all()
    DEF = players.filter(id__in = [ player.id for player in player_more]).all()

    player_more = PlayerMore.objects.filter(playing_possition1 = 'MID').all()
    MID = players.filter(id__in = [ player.id for player in player_more]).all()

    player_more = PlayerMore.objects.filter(playing_possition1 = 'STR').all()
    STR = players.filter(id__in = [ player.id for player in player_more]).all()

    _GK, _DEF, _MID, _STR = [], [], [], []
    for player in GK:
        _GK.append(player)

    for player in DEF:
        _DEF.append(player)

    for player in MID:
        _MID.append(player)

    for player in STR:
        _STR.append(player)

    random.shuffle(_GK)
    classified["GK"] = _GK
    random.shuffle(_DEF)
    classified["DEF"] = _DEF
    random.shuffle(_MID)
    classified["MID"] = _MID
    random.shuffle(_STR)
    classified["STR"] = _STR

    print(_DEF)

    return classified
