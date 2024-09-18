import pytest # type: ignore
from django.urls import reverse # type: ignore
from rest_framework.test import APIClient # type: ignore
from ..models import Room, UserRegistration
from django.utils import timezone # type: ignore
from datetime import timedelta
from django.contrib.auth.models import User # type: ignore

pytestmark = pytest.mark.django_db

def test_room_availability_check_case_unavaliable():
    client = APIClient()
    user=User.objects.create(username='lihekal',password='12345678910')
    
    room = Room.objects.create(room_number="101",avaliable=True,room_type='Single room',bed_count=1,bath_count=1,price_per_night=50)
    room_id=room.id
    room_object = Room.objects.get(pk=room_id)

    today = timezone.now().date()
    booking_start = today
    booking_end = today + timezone.timedelta(days=2)
    booking = UserRegistration.objects.create(customer=user.customer, room=room, startdate=booking_start, enddate=booking_end)

    # Authenticate the client
    client.force_authenticate(user=user)
    # Construct the URL for booking creation (assuming `bookings-list`)
    url = reverse('bookings-list')

    # Try to create a booking with overlapping dates
    data = {'startdate': booking_start, 'enddate': booking_end, 'room': room.id}
    response = client.post(url, data, format='json')

    # Assert that the response status code indicates an error (e.g., 400 Bad Request)
    assert response.status_code == 404
    
    


def test_room_availability_check_case_avaliable():
    client = APIClient()
    user=User.objects.create(username='ahmed',password='1122334455')
    client.force_authenticate(user=user)
    room = Room.objects.create(room_number="101",avaliable=True,room_type='Single room',bed_count=1,bath_count=1,price_per_night=50)
    room_id=room.id
    room_object = Room.objects.get(pk=room_id)

    today = timezone.now().date()

    UserRegistration.objects.create(customer=user.customer,room = room_object, startdate=today, enddate=today + timedelta(days=3))
    url = reverse('bookings-list')
    # Test case 2: Room should be available outside the booking dates
    response = client.get(url, {'startdate': today + timedelta(days=4), 'enddate': today + timedelta(days=6)})
    assert response.status_code == 200


