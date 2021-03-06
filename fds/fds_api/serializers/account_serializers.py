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
        if request is not None:
            if request.method == 'PUT' or request.method == 'PATCH':
                fields['dob'].read_only = True
                fields['gender'].read_only = True
                fields['birth_certificate'].read_only = True
        return fields



class PlayerSerializer(serializers.ModelSerializer):
    more = PlayerMoreSerializer()
    old_password = serializers.CharField(required=False)

    class Meta:
        fields = ['id', 'username', "email", 'password', 'old_password','profile_picture', 'first_name', 'last_name', 'phone_number', 'address' , 'type', 'more']
        read_only_fields = ['id', 'type']
 
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = Player

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request", None)
        if request is not None:
            if request.method ==  'POST':
                fields.pop('old_password')
        return fields

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

        if 'password' in validated_data.keys() and 'old_password' in validated_data.keys():
            if validated_data['old_password'] == instance.password:
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
        if request is not None:
            if request.method == 'PUT' or request.method == 'PATCH':
                fields['website'].read_only = True
        return fields


class ClubSerializer(serializers.ModelSerializer):
    more = ClubMoreSerializer()
    old_password = serializers.CharField(required=False)

    class Meta:
        fields = ['id', 'username', "email", 'scouts', 'old_password','profile_picture', 'phone_number', 'address', 'type', 'more']
        read_only_fields = ['id', 'type', 'scouts']
        

        # extra_kwargs = {
        #     'password': {'write_only': True},
        # }
        model = Club
        depth = 1

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request", None)
        if request is not None:
            if request.method ==  'POST':
                fields.pop('old_password')
        return fields

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
        
       
        if 'password' in validated_data.keys() and 'old_password' in validated_data.keys():
            if validated_data['old_password'] == instance.password:
                validated_data['password'] = make_password(validated_data['password'])


        return super().update(instance, validated_data)

############# scout serializer ##################

class ScoutMoreSerializer(serializers.ModelSerializer):
    # club = ClubSerializer()
    class Meta:
        fields = ['dob', 'gender', 'club', 'is_assigned']
        read_only_fields = ['club']

        model = ScoutMore
        depth = 1
        
        
        


    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request", None)
        if request is not None:
            if request.method == 'PUT' or request.method == 'PATCH':
                fields['dob'].read_only = True
                fields['gender'].read_only = True
            
        return fields


class ScoutSerializer(serializers.ModelSerializer):
    more = ScoutMoreSerializer()
    old_password = serializers.CharField(required=False)
    
    class Meta:
        fields = ['id', 'username', "email", 'password', 'old_password', 'profile_picture', 'first_name', 'last_name', 'phone_number', 'address' , 'type', 'more']
        read_only_fields = ['id', 'type']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = Scout
        
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request", None)
        if request is not None:
            if request.method ==  'POST':
                fields.pop('old_password')
        return fields

    def create(self, validated_data):
        # keeping "more" before poping it to create the basic scout account
        more = validated_data['more']
        validated_data.pop('more')
      
        club = self.context['request'].user
        
        #creating scout without more information
        validated_data['password'] = make_password(validated_data['password'])
        scout = Scout.objects.create(**validated_data)

        
        #adding "more property"
        more['id'] = scout.id
        more['account'] = scout
        more['club'] = club
        ScoutMore.objects.create(**more)

        
        
        return scout

    def update(self, instance, validated_data):
        
        if 'more' in validated_data.keys():
            more = validated_data['more']
            instance.more.__dict__.update(more)
            instance.more.save()
            validated_data.pop('more')

        if 'password' in validated_data.keys() and 'old_password' in validated_data.keys():
            if validated_data['old_password'] == instance.password:
                validated_data['password'] = make_password(validated_data['password'])

        return super().update(instance, validated_data)

    


########### Admin serializer ###################
# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ['id', 'username', 'phone_number', 'address', 'type']
#         read_only_fields = ['id', 'type']
#         model = Admin