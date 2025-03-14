from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.DateField()
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
