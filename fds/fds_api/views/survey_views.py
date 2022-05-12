from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..permissions import *
from ..models import * 
from ..serializers import *
from django.shortcuts import get_object_or_404


class QuestionView(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()




class AnswerView(viewsets.ViewSet):
    
    def create(self, request):
        player = get_object_or_404(Player, pk=2)
        answers = dict(request.data)
        
        for answer in answers:
            question = get_object_or_404(Question, pk=answer)
            Answer.objects.create(question=question, answer=answers[answer], player_id=player)

        return Response({"message": "Saved survey data."})

    def retrieve(self, request, pk=None):
        queryset = Answer.objects.all()
        user = get_object_or_404(Player, pk=pk)
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)
       
