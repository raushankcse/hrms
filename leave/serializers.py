from rest_framework import serializers

from leave.models import LeaveTypes


class LeaveTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveTypes
        fields = '__all__'
