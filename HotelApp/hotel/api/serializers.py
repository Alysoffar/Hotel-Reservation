from rest_framework import serializers # type: ignore
from hotel.models import Hotel

class HotelSerializer (serializers.ModelSerializer):
    class meta:
        model = Hotel
        fields = '__all__'