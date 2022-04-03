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

class ClubSerializer(serializers.ModelSerializer):
    more = ClubMoreSerializer()
    
    
    class Meta:
        fields = ['id', 'username', 'scouts', 'password', 'phone_number', 'address', 'type', 'more']
        read_only_fields = ['id', 'type', 'scouts']

        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = Club
