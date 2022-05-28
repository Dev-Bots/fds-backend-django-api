from rest_framework import viewsets
from rest_framework.response import Response
from ..models import *
from django.contrib.auth.hashers import make_password


class DataFill(viewsets.ViewSet):


    def create(self, request):
        import datetime
        # data entry

        for i in range(19):
            account = Player.objects.create(password=make_password('1234'), username=f"kevin{i}", email=f"k{i}@gmail.com", first_name="kevin", last_name="kevin", phone_number="12345", address='address')
            PlayerMore.objects.create(account=account, gender="MALE", dob=datetime.datetime.now(), overview="overview", education_level="highschool", foot="RIGHT", weight=80, height=175, playing_possition1="GK", playing_possition2="GK")
        for i in range(38):
            account = Player.objects.create(password=make_password('1234'), username=f"kevin{100+i}", email=f"k{100+i}@gmail.com", first_name="kevin", last_name="kevin", phone_number="12345", address='address')
            PlayerMore.objects.create(account=account, gender="MALE", dob=datetime.datetime.now(), overview="overview", education_level="highschool", foot="RIGHT", weight=80, height=175, playing_possition1="DEF", playing_possition2="DEF")
        for i in range(57):
            account = Player.objects.create(password=make_password('1234'), username=f"kevin{200+i}", email=f"k{200+i}@gmail.com", first_name="kevin", last_name="kevin", phone_number="12345", address='address')
            PlayerMore.objects.create(account=account, gender="MALE", dob=datetime.datetime.now(), overview="overview", education_level="highschool", foot="RIGHT", weight=80, height=175, playing_possition1="MID", playing_possition2="MID")
        for i in range(20):
            account = Player.objects.create(password=make_password('1234'), username=f"kevin{300+i}", email=f"k{300+i}@gmail.com", first_name="kevin", last_name="kevin", phone_number="12345", address='address')
            PlayerMore.objects.create(account=account, gender="MALE", dob=datetime.datetime.now(), overview="overview", education_level="highschool", foot="RIGHT", weight=80, height=175, playing_possition1="STR", playing_possition2="STR")  


        for i in range(10):
            club = Club.objects.create(password=make_password('1234'), username=f"club{i}", email=f"club{i}@gmail.com", phone_number="12345", address='address')
            ClubMore.objects.create(website="www.club.com", account=club, club_name=f"club{i}", acronym="CLUB", establishment_year=datetime.datetime.now(), organization_type="club")
        
        for i in range(20):
            account = Scout.objects.create(password=make_password('1234'), username=f"scout{i}", email=f"scout{i}@gmail.com", first_name="scout", last_name="scout", phone_number="12345", address='address')
            ScoutMore.objects.create(club_id = club.id, account=account, gender="MALE", dob=datetime.datetime.now())

        for i in range(5):
            Event.objects.create(club=club, starting_date=datetime.datetime.now(), application_deadline=datetime.datetime.now(), description="Description text", required_positions="ANY", age_limit=20, education_level="level of edu", session_time_for_each=20)
        
        return Response("Data entered.")