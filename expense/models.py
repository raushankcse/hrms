from django.db import models

from employee.models import Employees


# Create your models here.
class Expenses(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    expense_data = models.DateField()
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField()
    status = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(Employees, on_delete=models.CASCADE)

class Reimbursements(models.Model):
    expense_id = models.ForeignKey(Expenses, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255)
    processed_at = models.DateTimeField(auto_now_add=True)
