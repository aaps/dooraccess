from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):
    key = models.CharField(max_length=32)
    objects = UserManager()

    def save(self, *args, **kwargs):
      self.set_password(self.password)
      super(CustomUser, self).save(*args, **kwargs)


class Event(models.Model):
     name = models.CharField(max_length=32)
     description = models.CharField(max_length=200)
     startdate = models.DateField(blank=False, null=False)
     stopdate = models.DateField(blank=False, null=False)
     users = models.ForeignKey(CustomUser)


    
