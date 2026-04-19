from django.db import models

from employee.models import Employees


# Create your models here.
class TravelRequests(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    purpose = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    destinations = models.CharField(max_length=255)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    approved_by = models.ForeignKey(Employees, on_delete=models.CASCADE)

class TravelExpenses(models.Model):
    travel_id = models.ForeignKey(TravelRequests, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)

    description = models.TextField()