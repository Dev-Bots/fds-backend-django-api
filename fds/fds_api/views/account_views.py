from rest_framework import generics, permissions, viewsets


from ..permissions import *
from ..models import Player, Club, Scout
from ..serializers import PlayerSerializer, ClubSerializer, ScoutSerializer