from rest_framework import serializers # type: ignore
from RoomsBooking.models import Room ,UserRegistration

class RoomSerializer (serializers.ModelSerializer):
    class meta:
        model = Room
        fields = '__all__'


class BookingSerializer (serializers.ModelSerializer):

    startdate=serializers.DateField(required=True)
    enddate=serializers.DateField(required=True)
    class Meta:
        model = UserRegistration
        fields = ['startdate','enddate']
    
        
