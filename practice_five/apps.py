from django.apps import AppConfig


class PracticeFiveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'practice_five'

    def ready(self):
        import practice_five.signals

