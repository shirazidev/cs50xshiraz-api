from django.db import models



class Navbar(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title
    
    
class FooterLinks(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title
    
class SocialFooter(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    icon = models.FileField(upload_to='social', blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    


class Event(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    photo = models.FileField(upload_to='events', blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
class Sponsor(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    icon = models.FileField(upload_to='sponsors/icons', blank=True, null=True)
    photo = models.FileField(upload_to='sponsors/photos', blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    
class QA(models.Model):
    title = models.CharField(max_length=500)
    answer = models.TextField()
    
    def __str__(self):
        return self.title
    
    

    