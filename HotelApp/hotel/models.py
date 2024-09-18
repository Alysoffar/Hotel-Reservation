from django.db import models # type: ignore
from django.urls import reverse  # type: ignore
from django.utils import timezone # type: ignore
from PIL import Image # type: ignore


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.IntegerField()
    RestaurantsBarsNo = models.IntegerField()
    Satisfied_Guests = models.IntegerField()

