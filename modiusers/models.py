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
from django.contrib.auth.signals import (
    user_logged_in, user_logged_out, user_login_failed
) 
from django.utils import timezone

import uuid


def last_invalid_log():
    last = LogEntry.objects.filter(validentry = False)
    if last.exists():
        return list(last.all())[-1].doorkey
    else:
        return uuid.uuid1().hex


class CustomUser(AbstractUser):
    objects = UserManager()
    doorkey = models.CharField(max_length=32,unique=True,default=last_invalid_log )
    
    image = models.ImageField(max_length=255, upload_to="profiles/", null=True, blank=True, default="img/default_profile_image.png")

    def save(self, *args, **kwargs):
        # pdb.set_trace()
        super(CustomUser, self).save(*args, **kwargs)

  

class LogEntry(models.Model):
    doorkey = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    time = models.DateTimeField(default=timezone.now)
    validentry = models.BooleanField(default=False)



def log_user(sender, request, user, **kwargs):
    if isinstance(user, CustomUser):
        log = LogEntry(doorkey=user.doorkey, name=user.username)
        log.validentry = True
        log.save()

def log_bad_user(sender, **kwargs):
    log = LogEntry(doorkey=kwargs['credentials']['extra'], name='UNKNOWN')
    log.validentry = False
    log.save()

user_login_failed.connect(log_bad_user)
user_logged_in.connect(log_user)

@receiver(post_delete, sender=CustomUser)
def post_delete_user(sender, instance, *args, **kwargs):
    instance.image.delete(save=False)
        
