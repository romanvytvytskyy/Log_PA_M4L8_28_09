from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    question = models.CharField( max_length=255)
    voted_user = models.ManyToManyField(
         User, 
         related_name='voted-polls', blank=True
        )

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