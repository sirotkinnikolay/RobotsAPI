from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from RobotsAPI.excel_file_generate import exel_generate
from rest_framework.response import Response


class RobotViewSet(ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class WaitingListViewSet(ModelViewSet):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer


class RobotStatisticsViewSet(APIView):
    def get(self, request):
        return exel_generate()


class UrlViewSet(APIView):
    def get(self, request):
        url = Url.objects.all()
        return Response(UrlSerializer(url, many=True).data)

