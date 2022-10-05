from random import choices
from django.db import models
from user.enums import Role

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    role = models.CharField(choices=Role.choices(), max_length=50, default=Role.USER.value)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username