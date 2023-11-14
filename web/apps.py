# --------------------------------------------------------------------------- #
# Django exceptions
from django.apps import AppConfig
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# For saving discount information
class FurnitureConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "web"

    def ready(self):
        from .signals import real_price
# --------------------------------------------------------------------------- #