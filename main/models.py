from django.db import models

# Create your models here.


class Student(models.Model):

    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=25, default="")
    GPA = models.DecimalField(max_digits=4, decimal_places=3, default="")
    address = models.CharField(max_length=250, default="123 st")
    Date = models.CharField(max_length=15, default="")
    level = models.PositiveSmallIntegerField(default="0")
    Gender = models.CharField(max_length=50)
    email = models.EmailField(default="")
    mobile_number = models.CharField(max_length=20, default="011")
    department = models.CharField(max_length=10, default="AI")
    Status = models.CharField(max_length=50, default="Inactive")
