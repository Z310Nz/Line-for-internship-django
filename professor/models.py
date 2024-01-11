from django.contrib.auth.models import AbstractUser
from django.db import models

class Professor(AbstractUser):
    password = models.CharField(max_length=128, default='adminup1234')
    username =models.CharField(max_length=128, default='adminupse', unique=True)

    def __str__(self):
        return self.username