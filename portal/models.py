from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Qna(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=450)

    def __str__(self):
        return self.answer