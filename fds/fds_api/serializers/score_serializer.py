from django.forms import fields
from rest_framework import serializers
from ..models import *

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


    def create(self, validated_data):
        # if Grade.objects.filter(event__id = validated_data['event'].id, player__id = validated_data['player'].id, scout__id = validated_data['scout'].id).first():
        #     return False
        grade = Grade.objects.create(**validated_data)
        grade.aggregate = grade.calculate_aggregate()
        grade.save()
        return grade