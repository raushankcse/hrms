from django.db import models

from employee.models import Employees


# Create your models here.

class Attendance(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)

    attendance_date = models.DateField()
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now_add=True)

    total_hours = models.DecimalField(max_digits=5, decimal_places=2)

    status = models.CharField()

    is_late = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=["employee_id", "attendance_date"]),
        ]



class Holidays(models.Model):
    holidays_date = models.DateField()
    holidays_name = models.TextField()
    is_national = models.BooleanField(default=False)

