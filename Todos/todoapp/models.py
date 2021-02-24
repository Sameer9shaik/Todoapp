from django.db import models
# from .views import*
from django.contrib.auth.models import User


class Task(models.Model):
    Title = models.CharField(max_length=200)
    Time = models.DateField(auto_now_add=True)
    # status = models.CharField(max_length=100)
    Task_type = (
        ('l', 'Longterm'),
        ('s', 'shortterm'),
     )
    type = models.CharField(max_length=1, choices=Task_type)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.Title


