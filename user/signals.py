from django.db.models.signals import post_save
from .models import CustomUser
from django.dispatch import receiver
from order.models import UserCard


@receiver(post_save, sender=CustomUser)
def create_user_card(sender, instance, created, **kwargs):
    if created:
        UserCard.objects.create(user=instance)
