from django.db import models
from django.contrib.auth.models import User


# Create your models here.


def user_preview_directory_path(instance: 'Profile', filename: str) -> str:
    return 'users/instance.user_{pk}/users_avatars/{filename}'.format(
        pk=instance.user.pk,
        filename=filename,
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_acceptedc=models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_preview_directory_path) # type: ignore
    