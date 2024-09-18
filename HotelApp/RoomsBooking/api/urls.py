from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import RoomViewset , BookingViewset,UserBookingset ,BookingUpdateViewset ,BookingDeleteset

router = DefaultRouter()

router.register('room', RoomViewset , basename='roomview')
router.register('booking', BookingViewset , basename='bookings')
router.register('user_bookings', UserBookingset , basename='userbookings')
router.register('booking_update', BookingUpdateViewset , basename='updatebooking')
router.register('booking_delete', BookingDeleteset , basename='deletebooking')

urlpatterns = [
     
]+router.urls
