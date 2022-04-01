from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..permissions import *
from ..models import Event, Player
from ..serializers import EventSerializer

class Events(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventActions(viewsets.ViewSet):

    #pk of event and request.data[player_ids]
    @action(methods=['post'], detail=True)
    def approve_as_candidates(self, request, pk=None):
        event = get_object_or_404(Event, id=pk)

        to_be_candid_players = request.data['players']
        if to_be_candid_players:
            for player_id in to_be_candid_players:
                player = Player.objects.filter(id=player_id).first()
                if(player):
                    if(player in event.applicants.all()):
                        event.candidates.add(player)
                        event.save()
                    else:
                        return Response({"Message": "Player not in the list of applicants for the event."}, status=status.HTTP_403_FORBIDDEN)    
                else:
                    continue
            return Response({"Message": "Succesfully added players to the event."}, status=status.HTTP_202_ACCEPTED)
        return Response({"Message": "Error, problem with the list of players provided."}, status=status.HTTP_406_NOT_ACCEPTABLE)
