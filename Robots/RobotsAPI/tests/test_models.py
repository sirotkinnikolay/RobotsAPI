from django.test import TestCase
from RobotsAPI.models import Robot, RobotsModels
from datetime import datetime
from django.core.exceptions import ValidationError
import cProfile
import pstats
from io import StringIO
import sys


class RobotModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pr = cProfile.Profile()
        pr.enable()

        robot_model = RobotsModels.objects.create(robot_model='R2')
        Robot.objects.create(model=robot_model, version='N2', created=datetime.today(), availability=True)

        pr.disable()
        s = StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        with open('profile.txt', 'a') as f:
            f.write(s.getvalue())

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


