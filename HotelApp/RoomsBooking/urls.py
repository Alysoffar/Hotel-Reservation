from django.urls import path ,include# type: ignore
from . import views
from .views import  BookingCancelView,BookingUpdate

urlpatterns = [
    path('api/roomsbooking/', include('RoomsBooking.api.urls')),
    path('rooms/', views.room, name='rooms'),
    path('rooms/booking/<int:room_id>/', views.book, name='booking_page'),
    path('booking_view/', views.user_bookings, name='booking_view'),
    path('booking_view/<int:pk>/update/', BookingUpdate.as_view(), name='booking_update'),
    path('booking_view/<int:pk>/delete/', BookingCancelView.as_view(), name='booking_cancel'),
    
]
