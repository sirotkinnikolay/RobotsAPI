from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from RobotsAPI.views import RobotViewSet, WaitingListViewSet, RobotStatisticsAPIView, UrlAPIView
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'robot', RobotViewSet)
router.register(r'wait', WaitingListViewSet)

urlpatterns = [
    path('', UrlAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/stat/', RobotStatisticsAPIView.as_view()),
]
