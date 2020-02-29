from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120)
    rating = models.IntegerField()
    attendees = models.ListTextField(
        base_field = models.TextField(),
        size = 100
    )
    location = models.TextField(mex_length=120)
    
    def __str__(self):
        return self.title