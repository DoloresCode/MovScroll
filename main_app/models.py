from django.db import models

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