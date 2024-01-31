from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
USER_MODEL = get_user_model()
class Student(USER_MODEL):
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    line_id = models.CharField(max_length=200)
    website = models.URLField()
    cv = models.URLField()
    intern_job = models.CharField(max_length=200)
    intern_des = models.CharField(max_length=200)
    intern_company = models.CharField(max_length=200)
    interest_job = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    gpa = models.CharField(max_length=10)
    intern_start = models.DateField()
    intern_end = models.DateField()
    eng_skill = models.CharField(max_length=200)
    id_line = models.CharField(max_length=255, blank=True)
    access_token = models.CharField(max_length=255, blank=True)
    user_role = models.CharField(max_length=255, default='student', blank=True)
    # Add other fields as needed

    def __str__(self):
        return self.name