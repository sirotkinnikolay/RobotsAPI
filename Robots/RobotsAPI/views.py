from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
import xlsxwriter
from rest_framework.response import Response
from datetime import datetime, timedelta
import io
from django.http import HttpResponse


class RobotViewSet(ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class WaitingListViewSet(ModelViewSet):
    queryset = WaitingList.objects.all()
    serializer_class = WaitingListSerializer


class RobotStatisticsAPIView(APIView):
    def get(self, request):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
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
        for robot_mod_ver_count in robot_list.items():
            worksheet.write(i, 0, robot_mod_ver_count[0].split('-')[0])
            worksheet.write(i, 1, robot_mod_ver_count[0].split('-')[1])
            worksheet.write(i, 2, robot_mod_ver_count[1])
            i += 1

        workbook.close()
        output.seek(0)
        filename = 'statistics.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response


class UrlAPIView(APIView):
    def get(self, request):
        url = Url.objects.all()
        return Response(UrlSerializer(url, many=True).data)

