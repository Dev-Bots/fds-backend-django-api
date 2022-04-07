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
        model = Player
    def create(self, validated_data):
        # keeping "more" before poping it to create the basic player account
        more = validated_data['more']
        validated_data.pop('more')

        #creating player without more information
        validated_data['password'] = make_password(validated_data['password'])
        player = Player.objects.create(**validated_data)

        #adding "more property"
        more['account'] = player
        PlayerMore.objects.create(**more)
        
        return player

    def update(self, instance, validated_data):
        if 'more' in validated_data.keys():
            more = validated_data['more']
            instance.more.__dict__.update(more)
            instance.more.save()
            validated_data.pop('more')

        if 'password' in validated_data.keys():
                validated_data['password'] = make_password(validated_data['password'])

        return super().update(instance, validated_data)

############# club serializer ##################

class ClubMoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['club_name', 'acronym', 'organization_type' ,'website', 'establishment_year']
        model = ClubMore

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request", None)
        if request.method == 'PUT' or request.method == 'PATCH':
            fields['website'].read_only = True
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

    def create(self, validated_data):
        
        # keeping "more" before poping it to create the basic club account
        more = validated_data['more']
        validated_data.pop('more')


        #creating club without more information
        validated_data['password'] = make_password(validated_data['password'])
        club = Club.objects.create(**validated_data)

        #adding "more property"
        more['account'] = club
        ClubMore.objects.create(**more)
        
        return club

    def update(self, instance, validated_data):
        
        if 'more' in validated_data.keys():
            more = validated_data['more']
            instance.more.__dict__.update(more)
            instance.more.save()
            validated_data.pop('more')

        if 'password' in validated_data.keys():
                validated_data['password'] = make_password(validated_data['password'])

        return super().update(instance, validated_data)

