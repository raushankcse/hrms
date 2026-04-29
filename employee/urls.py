

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from employee.views import EmployeeCreateView, DepartmentViewSet, DesignationViewSet, MyEmployeeView, EmployeeListView

router = DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("designations", DesignationViewSet)


urlpatterns = [
    path('create_employee/', EmployeeCreateView.as_view()),
    path("", include(router.urls)),
    path("me/", MyEmployeeView.as_view()),
    path("admin/employees/", EmployeeListView.as_view()),
]


