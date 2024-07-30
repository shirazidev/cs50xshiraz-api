from django.contrib import admin
from . import models

class TeamSocialInLine(admin.TabularInline):
    model = models.TeamSocial
    
    
    
@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Team._meta.fields]
    inlines = [TeamSocialInLine]