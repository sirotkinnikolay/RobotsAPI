from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from RobotsAPI.views import RobotViewSet, WaitingListViewSet, RobotStatisticsAPIView

router = routers.SimpleRouter()
router.register(r'robot', RobotViewSet)
router.register(r'wait', WaitingListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/stat/', RobotStatisticsAPIView.as_view()),
]
