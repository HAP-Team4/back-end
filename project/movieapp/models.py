from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    movie_id = models.TextField(max_length=120, blank=True, null=True)
    genre  = models.TextField(max_length=120, blank=True, null=True)
    date = models.TextField(max_length=120, blank=True, null=True)
    time = models.TextField(max_length=120, blank=True, null=True)
    location = models.TextField(max_length=120, blank=True, null=True)
    capacity = models.TextField(max_length=120, blank=True, null=True)
    attendees = models.TextField(max_length=120, blank=True, null=True)
    
    def __str__(self):
        return self.title

class User(models.Model):
    user_id = models.CharField(max_length=120)
    movie_list = models.TextField()
    attending = models.TextField()
    
    def __str__(self):
        return self.user_id