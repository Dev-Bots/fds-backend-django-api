from rest_framework import serializers
from ..models import *
from django.contrib.auth.hashers import make_password
from drf_writable_nested.serializers import WritableNestedModelSerializer


############### Player serializers ##########################
class PlayerMoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['overview', 'gender','dob', 'video', 'birth_certificate', 'education_level', 'highest_education_evidence', 'foot', 'weight', 'height', 'playing_possition1', 'playing_possition2']
        actions_readonly_fields = {
            ('update', 'partial_update') : ('overview','gender', 'dob', 'birth_certificate')
        }
        model = PlayerMore

    
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request", None)
        if request.method == 'PUT' or request.method == 'PATCH':
            fields['dob'].read_only = True
            fields['gender'].read_only = True
            fields['birth_certificate'].read_only = True
        return fields
