from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import CanCreateEmployee
from .serializers import EmployeeCreateSerializer


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