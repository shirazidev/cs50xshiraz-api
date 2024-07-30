# views.py
from rest_framework import viewsets
from .models import Navbar, FooterLinks, SocialFooter, Event, Sponsor, QA
from .serializers import NavbarSerializer, FooterLinksSerializer, SocialFooterSerializer, EventSerializer, SponsorSerializer, QASerializer
from core.permissions import IsAdminUserForPost

class NavbarViewSet(viewsets.ModelViewSet):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer
    permission_classes = [IsAdminUserForPost]

class FooterLinksViewSet(viewsets.ModelViewSet):
    queryset = FooterLinks.objects.all()
    serializer_class = FooterLinksSerializer
    permission_classes = [IsAdminUserForPost]

class SocialFooterViewSet(viewsets.ModelViewSet):
    queryset = SocialFooter.objects.all()
    serializer_class = SocialFooterSerializer
    permission_classes = [IsAdminUserForPost]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdminUserForPost]

class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [IsAdminUserForPost]

class QAViewSet(viewsets.ModelViewSet):
    queryset = QA.objects.all()
    serializer_class = QASerializer
    permission_classes = [IsAdminUserForPost]