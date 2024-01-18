from django.test import TestCase
from RobotsAPI.tasks import send_mail_celery
from Robots.celery import app
from celery.result import AsyncResult


class CeleryTestCase(TestCase):

    def test_send_mail(self):
        res = send_mail_celery.delay(email_ad='test@mail.ru', text='test_text')
        inspect_workers = app.control.inspect()

        self.assertEqual(next(iter(next(iter((inspect_workers.registered().values()))))),
                         'RobotsAPI.tasks.send_mail_celery')

        self.assertIsNotNone(res.id)
        self.assertEqual(AsyncResult(res.id).state, 'SUCCESS')



