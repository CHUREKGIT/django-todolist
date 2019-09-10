from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
   name = models.CharField(max_length=200, default='Your List')
   body = models.CharField(max_length=200)
   user = models.ForeignKey(User, on_delete = models.CASCADE, default="123")
