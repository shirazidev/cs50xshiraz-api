
from django.urls import path
from .views import NavbarView, FooterLinksView, SocialFooterView, EventView, SponsorView, QAView

urlpatterns = [
    path('navbar/', NavbarView.as_view(), name='navbar'),
    path('footerlinks/', FooterLinksView.as_view(), name='footerlink'),
    path('socialfooter/', SocialFooterView.as_view(), name='socialfooters'),
    path('events/', EventView.as_view(), name='events'),
    path('sponsors/', SponsorView.as_view(), name='sponsors'),
    path('qa/', QAView.as_view(), name='QA'),
]