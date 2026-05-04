from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsHrOnly
from leave.models import LeaveTypes
from leave.serializers import LeaveTypesSerializer


# Create your views here.

class LeaveTypesViewSet(viewsets.ModelViewSet):

    queryset =  LeaveTypes.objects.all()
    serializer_class = LeaveTypesSerializer
    permission_classes = [IsAuthenticated, IsHrOnly]

    
