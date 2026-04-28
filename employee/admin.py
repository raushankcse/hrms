from django.contrib import admin

from employee.models import Departments, Designations, Employee

# Register your models here.
admin.site.register(Departments)
admin.site.register(Designations)
admin.site.register(Employee)
