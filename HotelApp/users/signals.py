from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import Customer
from rest_framework.authtoken.models import Token # type: ignore
from django.contrib.auth.models import User # type: ignore




@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, email=instance.email, image='default.jpg')


@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)