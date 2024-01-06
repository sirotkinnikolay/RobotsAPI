from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly


class RobotViewSet(ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class WaitingListViewSet(ModelViewSet):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer
