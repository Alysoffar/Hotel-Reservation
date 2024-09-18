from django.db import models # type: ignore
from django.urls import reverse  # type: ignore
from django.utils import timezone # type: ignore
from PIL import Image  # type: ignore
from users.models import Customer
from datetime import datetime

from django.core.validators import MinValueValidator # type: ignore

class Room(models.Model):
    room_number = models.IntegerField(unique=True, null=True, blank=True)
    avaliable = models.BooleanField(default=True)
    room_type = models.CharField(max_length=50,default = "Economy")
    bed_count = models.IntegerField(null=True, blank=True)
    bath_count = models.IntegerField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2 , null=True, blank=True,default = 100)
    image = models.ImageField(default='room-1.jpg', upload_to='room_pics',null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
  
    def __str__(self):
        return f"{self.room_type} - Room {self.room_number}"
            
class UserRegistration(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE , default=1)
    startdate = models.DateField(default=datetime.now)
    enddate = models.DateField()
    
    @classmethod
    def is_available(self, startdate, enddate):
        # Check for overlapping bookings
        bookings = UserRegistration.objects.filter(
            room=self.room,
            startdate__lt=enddate,
            enddate__gt=startdate
        ).exclude(id=self.id)  
        
        return not bookings.exists()

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})