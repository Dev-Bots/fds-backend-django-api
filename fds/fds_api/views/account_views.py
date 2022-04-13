from rest_framework import generics, permissions, viewsets


from ..permissions import *
from ..models import Player, Club, Scout
from ..serializers import PlayerSerializer, ClubSerializer, ScoutSerializer

# Create your views here.

class Players(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
   
class Clubs(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class Scouts(viewsets.ModelViewSet):
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer   
    permission_classes = [IsClubOrScoutEditRetrive]

