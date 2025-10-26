from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    question = models.CharField( max_length=255)
    voted_users = models.ManyToManyField(
         User, 
         related_name='voted_polls', blank=True
        )
    
    def __str__(self):
        return self.question

class Option(models.Model):
    poll = models.ForeignKey(
         Poll, 
         related_name='options', 
         on_delete=models.CASCADE
        )
    text = models.CharField(
         max_length=255
        )
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.text