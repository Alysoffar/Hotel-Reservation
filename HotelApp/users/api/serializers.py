from rest_framework import serializers # type: ignore
from users.models import Customer

class CustomerSerializer (serializers.ModelSerializer):
    class meta:
        model = Customer
        fields = ['username', 'email']


class ProfileSerializer (serializers.ModelSerializer):
    class meta:
        model = Customer
        fields = ['image']        