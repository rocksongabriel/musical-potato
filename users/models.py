from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Model to represent a user"""
    
    voted = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# TODO - use the student id to log the students in
# TODO - generate random password to each student that will be emailed to them