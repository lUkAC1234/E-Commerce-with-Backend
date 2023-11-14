# --------------------------------------------------------------------------- #
# Django exceptions
from django.db.models.signals import pre_save
from .models import FurnitureModel
from django.dispatch import receiver
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# For saving discount information
@receiver(pre_save, sender=FurnitureModel)
def real_price(sender, instance, **kwargs):
    if instance.is_discount:
        instance.real_price = instance.price - (instance.discount / 100) * instance.price
    else:
        instance.real_price = instance.price
    return instance
# --------------------------------------------------------------------------- #