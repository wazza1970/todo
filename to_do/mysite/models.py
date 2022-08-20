
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



# Create your models here.
class ToDo(models.Model):

    def __str__(self):
        return self.todo
  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=250)
    created = models.DateField(default=datetime.now().date())
    completed = models.CharField(max_length=10, default=False)

# class Post(models.Model):
#     user = models.CharField(max_length=200)




   