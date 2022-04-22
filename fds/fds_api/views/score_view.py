from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..permissions import *
from ..models import * 
from ..serializers import SkillSerializer, ParameterSerializer, GradeSerializer


class SkillView(viewsets.ModelViewSet):
    
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = Skill.objects.filter(club=self.request.user)
        return queryset
    

class ParameterView(viewsets.ModelViewSet):
    queryset = Parameters.objects.all()
    serializer_class = ParameterSerializer

    #this is for the depth of the nested returned json
    def get_serializer_class(self):
        if self.request.method == "GET":
            self.serializer_class.Meta.depth = 1
        else:
            self.serializer_class.Meta.depth = 0
        return self.serializer_class



class GradeView(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    

class Results(viewsets.ViewSet):

    
    def list(self, request):
        event_id = request.data['event_id']
        queryset = Grade.objects.filter(event__id=event_id).all()
        player_ids = set([player.player.id for player in queryset])
        organized = {}

        for p_id in player_ids:
            query = Grade.objects.filter(event__id=event_id,player__id=p_id).all()
            organized[p_id] = (GradeSerializer(query, many=True).data)

            scout_aggs = [grade.aggregate for grade in queryset]
            average = sum(scout_aggs) / len(scout_aggs)
            organized['average'] = round(average)
            
        
        return Response(organized)



    #retrieve the aggregate for a single player 
    def retrieve(self, request, pk=None):
        event_id = request.data['event_id']
        queryset = Grade.objects.filter(player__id=pk, event__id=event_id)
        serializer = GradeSerializer(queryset, many=True)

        data = {}
        data['id'] = pk
        data['scores'] = serializer.data

        scout_aggs = [grade.aggregate for grade in queryset]
        average = sum(scout_aggs) / len(scout_aggs)

        data['average'] = round(average, 2)
        
        
        return Response(data)

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

