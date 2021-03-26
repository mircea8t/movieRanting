from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(selfs):
        import users.signals