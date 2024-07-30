from rest_framework import serializers
from .models import Navbar, FooterLinks, SocialFooter, Event, Sponsor, QA

class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'

class FooterLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterLinks
        fields = '__all__'

class SocialFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialFooter
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class QASerializer(serializers.ModelSerializer):
    class Meta:
        model = QA
        fields = '__all__'