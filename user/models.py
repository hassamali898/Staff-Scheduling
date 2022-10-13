from random import choices
from django.db import models
from user.enums import Role
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    role = models.CharField(choices=Role.choices(), max_length=50, default=Role.USER.value)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'username'

    objects = UserManager()
    # REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.username