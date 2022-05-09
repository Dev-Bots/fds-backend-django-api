from django.forms import fields
from rest_framework import serializers
from ..models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('question', 'choices',)
        model = Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Choice


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer