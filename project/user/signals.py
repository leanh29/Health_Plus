from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.dispatch import receiver
from .models import ProfileModel

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_group(sender, instance, created, **kwargs):
    if created:
        g1 = Group.objects.get(name='Patient')
        instance.groups.add(g1)