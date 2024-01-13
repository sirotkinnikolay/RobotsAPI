from django.test import TestCase
from RobotsAPI.models import Robot, RobotsModels
from django.urls import reverse
from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase


class RobotViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        robot_count = 10
        robot_model = RobotsModels.objects.create(robot_model='R2')
        for robot_num in range(robot_count):
            Robot.objects.create(model=robot_model, version=f'N{robot_num}', created=datetime.today(), availability=True)

    def test_create_robot(self):
        url = '/api/robot/'
        data = {'model': 'R2',
                'version': 'S2',
                'created': str(datetime.today()),
                'availability': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Robot.objects.count(), 11)
        self.assertEqual(Robot.objects.get(version='S2').model, 'R2')

    def test_get_robot(self):
        url = '/api/robot/'
        url_1 = '/api/robot/5/'
        response = self.client.get(url)
        response_1 = self.client.get(url_1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(Robot.objects.count(), 10)
        self.assertEqual(response_1.data['version'], 'N3')

    def test_delete_robot(self):
        url = '/api/robot/5/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Robot.objects.count(), 9)

    def test_put_robot(self):
        url = '/api/robot/7/'
        data = {'model': 'R2',
                'version': 'TEST-PUT_METHOD',
                'created': str(datetime.today()),
                'availability': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Robot.objects.get(id=7).version, 'TEST-PUT_METHOD')
