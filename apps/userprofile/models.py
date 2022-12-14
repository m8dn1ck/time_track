## importing the user authentication models from django to save creating a new set.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Userprofile(models.Model):
    #user:userprofile needs to be 1:1 for saving data to work
    user = models.OneToOneField(User, related_name='userprofile',on_delete=models.CASCADE)
    active_team_id = models.IntegerField(default=0)
    