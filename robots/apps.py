from django.apps import AppConfig


class RobotsConfig(AppConfig):
    name = 'robots'

    def robot_is_available(self):
        import api.signals
