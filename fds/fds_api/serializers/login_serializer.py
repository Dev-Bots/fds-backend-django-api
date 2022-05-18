from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ..models import Player, Club, Scout
from ..serializers import PlayerSerializer, ClubSerializer, ScoutSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        account_json = ""
        if self.user.type == 'PLAYER':
            player = Player.objects.filter(id = self.user.id).first()
            player_serializer = PlayerSerializer()
            account_json = PlayerSerializer.to_representation(player_serializer, player)

        if self.user.type == 'CLUB':
            club = Club.objects.filter(id = self.user.id).first()
            club_serializer = ClubSerializer()
            account_json = ClubSerializer.to_representation(club_serializer, club)

        if self.user.type == 'SCOUT':
            scout = Scout.objects.filter(id = self.user.id).first()
            scout_serializer = ScoutSerializer()
            account_json = ScoutSerializer.to_representation(scout_serializer, scout)
        
        data['account'] = account_json
        return data