# views.py
from rest_framework import viewsets
from .models import Team, TeamSocial
from .serializers import TeamSerializer, TeamSocialSerializer
from core.permissions import IsAdminUserForPost  # Import if using custom permission

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminUserForPost]  # Apply custom permission if needed

class TeamSocialViewSet(viewsets.ModelViewSet):
    queryset = TeamSocial.objects.all()
    serializer_class = TeamSocialSerializer
    permission_classes = [IsAdminUserForPost]  # Apply custom permission if needed