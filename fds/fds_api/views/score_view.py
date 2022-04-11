from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..permissions import *
from ..models import * 
from ..serializers import SkillSerializer, ParameterSerializer, GradeSerializer


class SkillView(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ParameterView(viewsets.ModelViewSet):
    queryset = Parameters.objects.all()
    serializer_class = ParameterSerializer

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
