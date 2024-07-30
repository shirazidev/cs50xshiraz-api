# serializers.py
from rest_framework import serializers
from .models import Team, TeamSocial

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'  # Include all fields in the serializer

class TeamSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamSocial
        fields = '__all__'  # Include all fields in the serializer