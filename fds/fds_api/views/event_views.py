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
    #api/event_actions/event_id/apply   !!!!!!permission needed desperately!!!!!!!!!!!!!
    @action(methods=['post'], detail=True)
    def apply(self, request, pk=None):
        event = get_object_or_404(Event, id=pk)
        player = get_object_or_404(Player, id=request.user.id)
        event.applicants.add(player)
        event.save()
        return Response({"Message": "Succesfully applied the event."}, status=status.HTTP_202_ACCEPTED)

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
   
     
    #data list of players needed
    @action(methods=['post'], detail=True)     
    def accept_players(self, request, pk=None):
        event = get_object_or_404(Event, id=pk)
        to_be_accepted = request.data['players']
        if to_be_accepted:
            for player_id in to_be_accepted:
                player = Player.objects.filter(id=player_id).first()
                if(player):
                    if(player in event.candidates.all()):
                        event.accepted_applicants.add(player)
                        event.save()
                    else:
                        return Response({"Message": "Player not in the list of candidates for the event."}, status=status.HTTP_403_FORBIDDEN)    
                else:
                    continue
            return Response({"Message": "Succesfully accepted the winners of the event."}, status=status.HTTP_202_ACCEPTED)
        return Response({"Message": "Error, problem with the list of players provided."}, status=status.HTTP_406_NOT_ACCEPTABLE)

   # def get_permissions(self):
    # """
    # Instantiates and returns the list of permissions that this view requires.
    # """
    # if self.action == 'list':
    #     permission_classes = [IsAuthenticated]
    # else:
    #     permission_classes = [IsAdminUser]
    # return [permission() for permission in permission_classes]
    

    

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


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
