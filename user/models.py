# models.py
from django.db import models
from django.contrib.auth.models import User
import os

def profile_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user/media/images/profile/<filename>
    return 'user/media/images/profile/{0}/{1}'.format(instance.user.id, filename)

class ProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to=profile_image_path)

    def save(self, *args, **kwargs):
        # Delete the old profile image when updating
        try:
            old_instance = ProfileImage.objects.get(pk=self.pk)
            if old_instance.profile_image:
                # Remove old profile image file
                os.remove(old_instance.profile_image.path)
        except ProfileImage.DoesNotExist:
            pass

        # Save the new profile image
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"Picture of the {self.user.first_name}" 