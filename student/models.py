from django.db import models

# Create your models here.

class Student(models.Model):
    # Your model fields go here
    name = models.CharField(max_length=100)
    # Add other fields as needed