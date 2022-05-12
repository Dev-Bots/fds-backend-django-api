from django.forms import fields
from rest_framework import serializers
from ..models import *


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Team

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Match