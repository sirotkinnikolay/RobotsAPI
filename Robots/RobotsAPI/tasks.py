from celery import *
from celery import Celery
import smtplib
import logging
from celery.utils.log import get_task_logger
from decouple import config

app = Celery('myapp', broker='redis://localhost:6379/0')

logger = get_task_logger('celery_logging')
logger.setLevel(logging.INFO)
handler_c = logging.FileHandler("celery_logging_file.log", mode='a')
formatter_c = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler_c.setFormatter(formatter_c)
logger.addHandler(handler_c)


@app.task
def send_mail_celery(email_ad, text):

    user = config("USER_SMTP_EMAIL")
    passwd = config("USER_SMTP_PASS")

    logger.info(f'Отправлен email на адрес: {email_ad} с текстом: {text}')

    server = "smtp.yandex.ru"
    port = 587
    subject = "Тестовое письмо."
    to = "sirotkin.nikola@mail.ru"
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'
    text = text

    body = "\r\n".join((f"From: {user}", f"To: {to}",
                        f"Subject: {subject}", mime, charset, "", text))

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user, passwd)
        smtp.sendmail(user, to, body.encode('utf-8'))
    except smtplib.SMTPException as err:
        logger.error(err)
        raise err
    except Exception as error:
        logger.error(error)
    finally:
        smtp.quit()
