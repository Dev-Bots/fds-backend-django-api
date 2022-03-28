from rest_framework import serializers
from ..models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        # fields = ['id', 'club', 'starting_date', '']
        fields = '__all__'