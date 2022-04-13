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

""" VIEWSET ACTIONS

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
"""

