from .models import User, ActivityPeriods
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriods
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
    activity = ActivitySerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'

