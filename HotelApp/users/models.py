from django.db import models # type: ignore
from django.urls import reverse # type: ignore
from django.utils import timezone # type: ignore
from PIL import Image # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',null=True, blank=True)
    email = models.EmailField(unique=True, blank=False) 
    card_number = models.CharField(max_length=16)
    card_expiry_date = models.CharField(max_length=5)  
    card_cvc = models.CharField(max_length=3)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})




