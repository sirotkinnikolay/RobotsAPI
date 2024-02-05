from django.test import TestCase
from RobotsAPI.excel_file_generate import exel_generate
from rest_framework import status


class Function_Test(TestCase):

    def test_function_result(self):
        ex_result = exel_generate()
        self.assertEquals(ex_result.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(ex_result.content)
