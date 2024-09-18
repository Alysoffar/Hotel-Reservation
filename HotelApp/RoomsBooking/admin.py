from django.contrib import admin # type: ignore


from . models import Room , UserRegistration

# Register your models here.

admin.site.register(Room)
admin.site.register(UserRegistration)