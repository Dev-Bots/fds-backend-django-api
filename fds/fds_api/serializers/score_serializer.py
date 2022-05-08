from django.forms import fields
from rest_framework import serializers
from ..models import *
from django.shortcuts import get_object_or_404

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'description', 'weight_for_GK', 'weight_for_DEF', 'weight_for_MID', 'weight_for_STR', 'is_default']
        read_only_fields = ['is_default']
    def create(self, validated_data):

        #getting club 
        club_id = self.context['request'].user.id
        club = get_object_or_404(Club, pk=club_id)

        skill= Skill.objects.create(club=club, **validated_data)
        return skill

"""
 club = models.ForeignKey('club', on_delete=models.CASCADE)
    name = models.CharField(_('Skill name'), max_length=100, blank=False)
    description = models.TextField(_("Skill Description"), blank=False)weight_for_GK

    weight_for_GK = models.IntegerField(_("Level of importance for GKs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_DEF = models.IntegerField(_("Level of importance for DEFs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_MID = models.IntegerField(_("Level of importance for MIDs"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)
    weight_for_STR = models.IntegerField(_("Level of importance for GK"), choices=SkillWeight.choices, default=SkillWeight.MODERATE)

"""

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        fields = '__all__'
        # depth = 1


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
        # read_only_fields = ['aggregate']

    def create(self, validated_data):
        # if Grade.objects.filter(event__id = validated_data['event'].id, player__id = validated_data['player'].id, scout__id = validated_data['scout'].id).first():
        #     return False
        grade = Grade.objects.create(**validated_data)
        grade.aggregate = grade.calculate_aggregate()
        grade.save()
        return grade