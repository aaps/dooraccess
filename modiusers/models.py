from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import (AbstractUser, PermissionsMixin)
import pdb
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
# from django.core.files.images import get_image_dimensions
from django.db.models.signals import pre_delete
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.signals import user_logged_in



class CustomUser(AbstractUser):
    objects = UserManager()
    doorkey = models.CharField(max_length=32, default="ffffff")
    
    image = models.ImageField(max_length=255, upload_to="profiles/", null=True, blank=True, default="img/default_profile_image.png")

    def save(self, *args, **kwargs):
        # pdb.set_trace()
        super(CustomUser, self).save(*args, **kwargs)

# class LogEntry(models.Model)

# def log_user(request, *args, **kwargs):
#     pass


# user_logged_in.connect(log_user)

@receiver(post_delete, sender=CustomUser)
def post_delete_user(sender, instance, *args, **kwargs):
    instance.image.delete(save=False)
        
