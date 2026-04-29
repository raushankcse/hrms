from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.exceptions import ValidationError
from .models import Employee, Departments, Designations

User = get_user_model()


class EmployeeCreateSerializer(serializers.Serializer):

    # 🔐 REQUIRED (always)
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=User.Role.choices)

    # 👤 OPTIONAL (HR can fill, Admin may skip)
    employee_code = serializers.CharField(required=False , allow_blank=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)

    department = serializers.IntegerField(required=False, allow_null=True)
    designation = serializers.IntegerField(required=False ,allow_null=True)
    location = serializers.CharField(required=False ,allow_blank=True)

    joining_date = serializers.DateField(required=False, allow_null=True)
    employment_type = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True)

    # 🔥 RBAC LOGIC
    def validate(self, data):
        creator = self.context["request"].user
        role = data.get("role")

        # Admin → ONLY HR
        if creator.role == "admin":
            if role != "hr":
                raise ValidationError("Admin can ONLY create HR")

        # HR → Manager + Employee
        elif creator.role == "hr":
            if role not in ["manager", "employee"]:
                raise ValidationError("HR can create Manager or Employee")

        else:
            raise ValidationError("Not allowed")

        # prevent duplicate email
        if User.objects.filter(email=data["email"]).exists():
            raise ValidationError("Email already exists")

        return data

    # 🔥 CREATE LOGIC
    def create(self, validated_data):
        email = validated_data.pop("email")
        role = validated_data.pop("role")

        with transaction.atomic():

            # 1️⃣ create user (no password yet)
            user = User.objects.create(email=email, role=role)
            user.set_unusable_password()
            user.save()

            # 2️⃣ create employee with partial data
            employee = Employee.objects.create(
                user=user,
                **validated_data
            )

        return employee



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designations
        fields = "__all__"

    def validate(self, data):
        if data["level"] < 1:
            raise serializers.ValidationError("Level must be >= 1")
        return data


class EmployeeSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source="user.email", read_only=True)
    role = serializers.CharField(source="user.role", read_only=True)

    department_name = serializers.CharField(source="department.name", read_only=True)
    designation_name = serializers.CharField(source="designation.name", read_only=True)
    

    class Meta:
        model = Employee
        fields = "__all__"