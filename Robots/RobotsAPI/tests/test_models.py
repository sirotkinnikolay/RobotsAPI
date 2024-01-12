from django.test import TestCase
from RobotsAPI.models import Robot, RobotsModels
from datetime import datetime
from django.core.exceptions import ValidationError


class RobotModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        robot_model = RobotsModels.objects.create(robot_model='R2')
        Robot.objects.create(model=robot_model, version='N2', created=datetime.today(), availability=True)

    def test_robot_model_values(self):
        robot = Robot.objects.get(id=1)
        self.assertEquals(robot.version, 'N2')
        self.assertEquals(robot.model, 'R2')

    def test_robot_model_max_length(self):
        robot = Robot.objects.get(id=1)
        max_length = robot._meta.get_field('model').max_length
        self.assertEquals(max_length, 200)

    def test_robot_model_update(self):
        robot = Robot.objects.get(id=1)
        robot.availability = False
        robot.save()
        self.assertEquals(robot.availability, False)

    def test_robot_model_validate(self):
        with self.assertRaises(ValidationError):
            robot = Robot.objects.get(id=1)
            robot.availability = 12345
            robot.save()




