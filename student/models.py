from django.db import models

# Create your models here.

class Student(models.Model):
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    student_id = models.IntegerField()
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.BooleanField()  # True: Male / False: Female
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
    # Add other fields as needed

    def __str__(self):
        return self.name