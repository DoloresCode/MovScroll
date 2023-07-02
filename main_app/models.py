from django.db import models
import time

# Create your models here.

class Actor(models.Model):

    name = models.CharField(max_length=400)
    img = models.CharField(max_length=700)
    bio = models.TextField(max_length=3000)
    verified_actor = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Movie(models.Model):

    img = models.CharField(max_length=700)
    title = models.CharField(max_length=3000)
    release_year = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(default=0)
    genre = models.CharField(max_length=3000)
    synopsis = models.CharField(max_length=3000)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.title

# Here we define the method to look at the length property and convert it
    def get_runtime(self):
        return time.strftime("%-M:%S", time.gmtime(self.runtime))
    
class Watchlist(models.Model):
    title = models.CharField(max_length=3000)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.title