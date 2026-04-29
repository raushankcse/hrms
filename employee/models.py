from django.conf import settings
from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Designations(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name



class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    employee_code = models.CharField(max_length=100, null=True, blank=True)


    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    phone = models.CharField(max_length=100,null=True, blank=True)

    department = models.ForeignKey(Departments, on_delete=models.CASCADE, blank=True, null=True)
    designation = models.ForeignKey(Designations, on_delete=models.CASCADE, blank=True, null=True)
    location = models.CharField(blank=True, null=True)

    joining_date = models.DateField(null=True, blank=True)
    employment_type = models.CharField(max_length=100, null=True,blank=True)
    status = models.CharField(max_length=100, null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"