from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver

from bookbar.profiles.models import Profile

UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


@receiver(signals.pre_save, sender=Profile)
def check_if_profile_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.phone_number:
        instance.is_complete = True
