from categories.models import Category
from django.db import models
from utils.models import TimeStampsModel


class Book(TimeStampsModel):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    publishedDate = models.DateField()
