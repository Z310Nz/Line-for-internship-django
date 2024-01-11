from django.db import models

# Create your models here.
class Company(models.Model):
    logoc = models.ImageField(upload_to='logos/', null=True, blank=True)
    company_name = models.CharField(max_length=255)
    foundation_date = models.DateField()
    company_type = models.CharField(max_length=255)
    number_of_employees = models.IntegerField()
    website = models.URLField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    address_label = models.CharField(max_length=255)
    line_id = models.CharField(max_length=255, blank=True)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, default='')
    workplace = models.CharField(max_length=255)
    worktype = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    benefit = models.CharField(max_length=255)
    workstart = models.TimeField()
    workend = models.TimeField()
    workday = models.CharField(max_length=255)

    # Add more fields for the company address here

    def __str__(self):
        return f"Job {self.id} for {self.company.company_name}"