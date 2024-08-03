from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   # Name, Email and Password will get from User 
    bio = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username