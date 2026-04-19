from django.db import models

from employee.models import Employees


# Create your models here.

class LeaveTypes(models.Model):
    name = models.TextField()
    is_paid = models.BooleanField(default=False)
    max_days = models.IntegerField()

class LeaveBalances(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    leave_type_id = models.ForeignKey(LeaveTypes, on_delete=models.CASCADE)

    total_allocated = models.IntegerField()
    used = models.IntegerField()
    remaining = models.IntegerField()

    year = models.IntegerField()

class Leaves(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    leave_type_id = models.ForeignKey(LeaveTypes, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.IntegerField()
    status = models.CharField(max_length=50)

    approved_by_manager = models.ForeignKey(Employees, on_delete=models.CASCADE)
    approved_by_hr = models.ForeignKey(Employees, on_delete=models.CASCADE)

