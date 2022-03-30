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