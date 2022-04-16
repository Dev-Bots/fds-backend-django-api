from rest_framework import serializers
from ..models import *

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ['account']

    def create(self, validated_data):
        validated_data['account'] = self.request.user
        notification = Notification.objects.create(validated_data)
        return notification