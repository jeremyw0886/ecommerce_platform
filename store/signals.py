from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserProfile

User = get_user_model()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Try to get the profile; if it doesn't exist, create it.
    profile, created_profile = UserProfile.objects.get_or_create(user=instance)
    # Optionally, update the profile here if needed.
    profile.save()
