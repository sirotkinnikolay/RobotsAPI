from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not email:
            raise ValueError('The Email field must be set')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', unique=True)
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class RobotsModels(models.Model):
    robot_model = models.CharField(max_length=200, verbose_name='модель робота')

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.robot_model


class Robot(models.Model):
    model = models.CharField(max_length=200, verbose_name='модель')
    version = models.CharField(max_length=200, verbose_name='версия')
    created = models.DateField(auto_now_add=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'Робот'
        verbose_name_plural = 'Роботы'

    def __str__(self):
        return str(self.created)


class WaitingList(models.Model):
    model_robot_wait = models.ForeignKey('RobotsModels', on_delete=models.CASCADE,
                                         verbose_name='модель робота ожидания')
    version_robot_wait = models.CharField(max_length=200, verbose_name='версия робота ожидания')
    user_waiting = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='ожидает пользователь')

    class Meta:
        verbose_name = 'Лист ожидания заказа'
        verbose_name_plural = 'Листы ожидания заказа'

    def __str__(self):
        return self.user_waiting.email
