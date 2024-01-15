from django.test import TestCase
from django.test.utils import override_settings
from RobotsAPI.tasks import send_mail_celery


class AddTestCase(TestCase):

    @override_settings(CELERY_EAGER_PROPAGATES_EXCEPTIONS=True,
                       CELERY_ALWAYS_EAGER=True,
                       CELERY_BROKER_URL="memory",
                       CELERY_RESULT_BACKEND="memory"
                       )
    def test_send_mail_celery(self):
        # TODO не проверить статус задачи Celery
        result = send_mail_celery.delay(email_ad="test@mail.ru", text='test_text')
        self.assertIsNotNone(result.id)
