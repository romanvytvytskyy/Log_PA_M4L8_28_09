from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва події")
    description = models.TextField(verbose_name="Опис")
    event_date = models.DateTimeField(verbose_name="Дата та час проведення", 
                                      default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['event_date']
        
    def __str__(self):
        return self.name
    
    