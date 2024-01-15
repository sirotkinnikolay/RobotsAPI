from django.test import TestCase
from RobotsAPI.models import Robot, RobotsModels
from RobotsAPI.serializers import RobotSerializer
from django.db.models import signals


class RobotSerializerTest(TestCase):
    def setUp(self):

        self.robot_attributes = {
            'model': 'R2',
            'version': 'S2',
            'created': '2024-01-13',
            'availability': True
        }

        self.serializer_data = {
            'model': 'R2',
            'version': 'T2',
            'created': '2024-01-13',
            'availability': False
        }

        self.robot = Robot.objects.create(**self.robot_attributes)
        self.serializer = RobotSerializer(instance=self.robot)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'model', 'version', 'created', 'id'})

    def test_version_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['version'], self.robot_attributes['version'])
        self.assertEqual(data['version'], 'S2')

