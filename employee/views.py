from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Departments, Designations, Employee

from accounts.permissions import CanCreateEmployee, IsAdminOnly
from .serializers import EmployeeCreateSerializer, DepartmentSerializer, DesignationSerializer, EmployeeSerializer


class EmployeeCreateView(APIView):
    permission_classes = [IsAuthenticated, CanCreateEmployee]

    def post(self, request):
        serializer = EmployeeCreateSerializer(
            data=request.data,
            context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        employee = serializer.save()

        return Response(
            {
                "message": "Employee created",
                "employee_id": employee.id
            },
            status=status.HTTP_201_CREATED
        )


class DepartmentViewSet(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.action in ["create", "update" , "partial_update", "destroy"]:
            return [IsAdminOnly()]
        return [IsAuthenticated()]

class DesignationViewSet(ModelViewSet):
    queryset = Designations.objects.select_related("department")
    serializer_class = DesignationSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminOnly()]
        return [IsAuthenticated()]


class MyEmployeeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not hasattr(request.user, "employee"):
            return Response(
                {"error": "Employee profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        employee = request.user.employee
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def patch(self, request):
        if not hasattr(request.user, "employee"):
            return Response(
                {"error": "Employee profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        employee = request.user.employee

        serializer = EmployeeSerializer(
            employee,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Profile updated successfully",
            "data": serializer.data
        })

class EmployeeListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOnly]

    def get(self, request):
        employees = Employee.objects.select_related(
            "user", "department", "designation"
        )

        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)