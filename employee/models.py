from django.conf import settings
from django.db import models

# Create your models here.

class Departments(models.Model):
    name = models.CharField(max_length=100)

class Designations(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField()


class Locations(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)


class Employees(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    employee_code = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)

    departemnt_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designations, on_delete=models.CASCADE)
    loaction_id = models.ForeignKey(Locations, on_delete=models.CASCADE)




    joining_date = models.DateField()
    employment_type = models.CharField(max_length=100)

    status = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)