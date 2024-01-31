from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
USER_MODEL = get_user_model()

class Professor(USER_MODEL):
    pass