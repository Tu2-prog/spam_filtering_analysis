"""Model classes for saving objects with certain structure into the database."""
from django.db import models


# Create your models here.
class User(models.Model):
    """User class to model a potential user of the spam_filtering_analysis application"""

    user_id = models.IntegerField(
        primary_key=True, blank=False, null=False, unique=True
    )
    username = models.CharField(max_length=70, blank=False, default="")
    password = models.CharField(max_length=100)
