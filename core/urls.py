# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from team.views import TeamViewSet, TeamSocialViewSet
from home.views import NavbarViewSet, FooterLinksViewSet, SocialFooterViewSet, EventViewSet, SponsorViewSet, QAViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="CS50xShiraz API",
        default_version='v1',
        description="API documentation for CS50xShiraz project",
        terms_of_service="https://shirazidev.ir",
        contact=openapi.Contact(email="info@shirazidev.ir"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'team-socials', TeamSocialViewSet)
router.register(r'navbars', NavbarViewSet)
router.register(r'footer-links', FooterLinksViewSet)
router.register(r'social-footers', SocialFooterViewSet)
router.register(r'events', EventViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'qas', QAViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]