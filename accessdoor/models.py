from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import (
     AbstractUser, PermissionsMixin
)

class CustomUser(AbstractUser):
    id = models.DecimalField(primary_key=True,decimal_places=2,max_digits=2)
    # key = models.CharField(max_length=32)
    objects = UserManager()
    # REQUIRED_FIELDS = ['date_of_birth', 'height', 'password']

    # def save(self, *args, **kwargs):
    #   self.set_password(self.password)
    #   super(CustomUser, self).save(*args, **kwargs)
    permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )


class Event(models.Model):
     name = models.CharField(max_length=32)
     description = models.CharField(max_length=200)
     startdate = models.DateField(blank=False, null=False)
     stopdate = models.DateField(blank=False, null=False)
     users = models.ForeignKey(CustomUser)

     # sdjkfhsdjhf/




     # dsfsdf