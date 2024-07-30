from django.contrib import admin
from .models import Navbar, FooterLinks, SocialFooter, Event, Sponsor, QA

# Register your models here.
admin.site.register(Navbar)
admin.site.register(FooterLinks)
admin.site.register(SocialFooter)
admin.site.register(Event)
admin.site.register(Sponsor)
admin.site.register(QA)