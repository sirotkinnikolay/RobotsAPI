from django.contrib import admin
from RobotsAPI.models import User,  RobotsModels, Robot, WaitingList
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


class RobotsModelsAdmin(admin.ModelAdmin):
    list_display = ['robot_model']


admin.site.register(RobotsModels, RobotsModelsAdmin)


class RobotAdmin(admin.ModelAdmin):
    list_display = ['model', 'version', 'created']


admin.site.register(Robot, RobotAdmin)


class WaitingListAdmin(admin.ModelAdmin):
    list_display = ['model_robot_wait', 'version_robot_wait', 'user_waiting']


admin.site.register(WaitingList, WaitingListAdmin)


admin.site.register(User, UserAdmin)
