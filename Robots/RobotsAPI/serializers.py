from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class RobotSerializer(ModelSerializer):
    class Meta:
        model = Robot
        fields = "__all__"

    def create(self, validated_data, **kwargs):
        validated_model = validated_data['model']
        if len(RobotsModels.objects.filter(robot_model=validated_model)) != 0:
            return Robot.objects.create(**validated_data)
        else:
            raise Exception(f"Модели: {validated_model} нет в базе")


class WaitingListSerializer(ModelSerializer):
    user_waiting = serializers.HiddenField(default=None)

    class Meta:
        model = WaitingList
        fields = "__all__"

    def create(self, validated_data, **kwargs):
        user = self.context['request'].user
        validated_data['user_waiting'] = user
        return WaitingList.objects.create(**validated_data)


class UrlSerializer(ModelSerializer):
    id = serializers.HiddenField(default=None)

    class Meta:
        model = Url
        fields = "__all__"
