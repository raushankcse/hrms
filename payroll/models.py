from django.db import models

from employee.models import Employees


# Create your models here.
class SalaryStructure(models.Model):
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)

    basic = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2)

    pf_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)


class Payroll(models.Model):

    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)

    month = models.DateField()

    total_working_days = models.IntegerField()

    present_days = models.IntegerField()

    leave_days = models.IntegerField()

    absent_days = models.IntegerField()

    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    generated_at = models.DateField()


class PaySlips(models.Model):
    payroll_id = models.ForeignKey(Payroll, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)

    file_url = models.URLField()







