from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
import xlsxwriter
from rest_framework.response import Response
from datetime import datetime, timedelta


class RobotViewSet(ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class WaitingListViewSet(ModelViewSet):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer


class RobotStatisticsAPIView(APIView):
    def get(self, request):

        workbook = xlsxwriter.Workbook('statistics.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, 'МОДЕЛЬ')
        worksheet.write(0, 1, 'ВЕРСИЯ')
        worksheet.write(0, 2, 'КОЛИЧЕСТВО ЗА НЕДЕЛЮ')

        startdate = datetime.today()
        enddate = startdate - timedelta(days=7)
        model_robots = RobotsModels.objects.all()

        robot_list = {}
        for m in model_robots:
            robots = Robot.objects.filter(created__range=[enddate, startdate]).filter(model=m.robot_model)

            for r in robots:
                if f'{m.robot_model} - {r.version}' in robot_list.keys():
                    robot_list[f'{m.robot_model} - {r.version}'] += 1
                else:
                    robot_list[f'{m.robot_model} - {r.version}'] = 1

        i = 1
        for robot in robot_list:
            ########################################################################
            worksheet.write(i, 0, robot)
            worksheet.write(i, 1, robot)
            worksheet.write(i, 2, '-------')
            i += 1

        workbook.close()
        return Response(f'{robot_list}')
