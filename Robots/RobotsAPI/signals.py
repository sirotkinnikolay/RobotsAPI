from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from RobotsAPI.tasks import send_mail_celery


@receiver(post_save, sender=Robot)
def send_email_on_post_save(sender, instance, created, **kwargs):
    if created:
        rob_mod = RobotsModels.objects.get(robot_model=instance.model)
        rob_ver = instance.version

        result = WaitingList.objects.filter(model_robot_wait=rob_mod, version_robot_wait=rob_ver).order_by('id')
        if len(result) != 0:
            first_wait_client = result.first().user_waiting
            text_for_client = (
                f'Добрый день.Недавно вы интересовались нашим роботом модели {rob_mod}, версии {rob_ver}.'
                f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами')

            send_mail_celery.delay(str(first_wait_client), text_for_client)
