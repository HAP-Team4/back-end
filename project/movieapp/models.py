from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120)
    location = models.TextField(max_length=120)
    attendees = models.TextField()
    
    def __str__(self):
        return self.title