from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
# from rest_framework.decorators import action
from ..permissions import *
from ..models import * 
from ..serializers import *
from django.shortcuts import get_object_or_404

from ..utils import *



class CheckTeamBuilder(viewsets.ViewSet):

     def retrieve(self, request, pk=None):
        players = Player.objects.all() #just query this from candidate pk must point to an event
        

        return Response(check_for_the_right_formation(players))

class BuildTeams(viewsets.ViewSet):

    def create(self, request):
        event = get_object_or_404(Event, request["event_id"])
        candidates = event.candidates
        print(candidates)
        players = Player.objects.all() #just query this from candidate pk must point to an event
        formation = check_for_the_right_formation(players)

        import datetime
        count = 0
        for additional_dummies in formation['required_numbers']:
            for i in range(formation['required_numbers'][additional_dummies]):
                account = Player.objects.create(password="1234", username=f"Dummy-{event.id}-{count}", email=f"dummy-{event.id}-{count}@gmail.com", first_name="Dummy", last_name="Data", phone_number="12345", address='address')
                PlayerMore.objects.create(account=account, gender="MALE", dob=datetime. datetime(2000, 9, 15), overview="overview", education_level="highschool", foot="RIGHT", weight=80, height=175, playing_possition1=additional_dummies, playing_possition2=additional_dummies)
                players |= Player.objects.filter(pk=account.id)
                count += 1

        classified_pos = classify_possition(players)

        GK = classified_pos["GK"]
        DEF = classified_pos["DEF"]
        MID = classified_pos["MID"]
        STR = classified_pos["STR"]
       
        
        
        no_of_teams = len(GK)
        form = formation['formation']
        form_to_string = ''
        for i in form:
            form_to_string += str(i) + " " 

        for i in range(no_of_teams):
            team =  Team.objects.create(formation=form_to_string, event=event)

            team.players.add(GK[0])
            GK.pop(0)

            for defs in range(form[0]):
                team.players.add(DEF[0])
                DEF.pop(0)
            for mids in range(form[1]):
                team.players.add(MID[0])
                MID.pop(0)
            for strs in range(form[2]):
                team.players.add(STR[0])
                STR.pop(0)
                

        return Response({"message": "Teams are built."})

class TeamView(viewsets.ReadOnlyModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class MakeMatch(viewsets.ViewSet):

    def create(self, request):
        event = get_object_or_404(Event, pk=request.data["event_id"])

        teams = Team.objects.all()
        teams_to_list = []
        for team in teams:
            teams_to_list.append(team)
        length = int(len(teams_to_list))
        half_len = int(length / 2)

        for team1, team2 in zip(teams_to_list[:half_len], teams_to_list[half_len:]):
            Match.objects.create(event=event, team1=team1, team2=team2)

        return Response({"message": "Matches created."})

class MatchView(viewsets.ReadOnlyModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()