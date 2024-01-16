from django.test import TestCase
from celery.contrib.testing.worker import start_worker
from celery import Celery
from RobotsAPI.tasks import send_mail_celery


class CeleryTestCase(TestCase):
    def setUp(self):
        self.app = Celery('myapp', broker='memory://', backend='memory://')

    def test_send_mail_celery(self):
        # TODO: ОШИБКА -------> assert 'celery.ping' in app.tasks
        with start_worker(app=self.app):
            result = send_mail_celery.apply_async(args=["test@mail.ru", "test_text"])
            result.get()
            print(result.status)


# Теперь вы можете добавить свои утверждения, чтобы проверить результат
# Например, можно проверить логирование или что-то еще.
# Пример:
# self.assertEqual(ожидаемый результат, фактический результат)
# self.assertIn("ожидаемая строка в логах", логи)

