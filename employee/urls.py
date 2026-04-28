from django.urls import path

from employee.views import EmployeeCreateView

urlpatterns = [
    path('create_employee/', EmployeeCreateView.as_view()),
]


