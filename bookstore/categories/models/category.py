from django.db import models

from utils.models import TimeStampsModel


class Category(TimeStampsModel):
    name = models.CharField(max_length=255)
