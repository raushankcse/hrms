from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model

User = get_user_model()


class CanCreateEmployee(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return user.role in [
            User.Role.ADMIN,
            User.Role.HR
        ]


class IsAdminOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return user.role == User.Role.ADMIN


class IsHrOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False
        return user.role == User.Role.HR