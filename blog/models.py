from django.db import models
from blogger.models import Blogger
# Create your models here.
    
class Blog(models.Model):
    title = models.TextField(max_length=300)
    abstract = models.TextField() 
    date = models.DateField(auto_now_add=True)
    blogger = models.ManyToManyField(Blogger)

    def __str__(self):
        return self.date
    
class React(models.Model):
    blog = models.ManyToManyField(Blog)
    blogger = models.ManyToManyField(Blogger)

    def __str__(self):
        return self.blog