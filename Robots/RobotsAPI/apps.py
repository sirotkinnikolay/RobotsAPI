from django.apps import AppConfig


class RobotsapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RobotsAPI'

    def ready(self):
        import RobotsAPI.signals
