from django.db import models
from dirtyfields import DirtyFieldsMixin


class Team(DirtyFieldsMixin, models.Model):
    TECHNICAL = "تیم فنی"
    CONTENTCREATEOR = "تیم تولید محتوا"
    MARKETING = "تیم مارکتینگ و روابط عمومی"
    PHOTOGRAPHY = "تیم عکاسی و فیلم برداری"
    EXECUTIVE = "تیم اجرایی"
    TEAM_CHOICES = [
        (TECHNICAL, "تیم فنی"),
        (CONTENTCREATEOR, "تیم تولید محتوا"),
        (MARKETING, "تیم مارکتینگ و روابط عمومی"),
        (PHOTOGRAPHY, "تیم عکاسی و فیلم برداری"),
        (EXECUTIVE, "تیم اجرایی"),
        
    ]
    name = models.CharField(max_length=300)
    photo = models.FileField(upload_to='team', blank=True, null=True)
    job = models.CharField(max_length=300)
    category = models.CharField(
        max_length=100,
        choices=TEAM_CHOICES,
        verbose_name="تیم"
    )
    
    def __str__(self):
        return self.name
    
    
    
class TeamSocial(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    icon = models.FileField(upload_to='team/social',)
    alt = models.CharField(max_length=300)
    
    def __str__(self):
        return self.team.name