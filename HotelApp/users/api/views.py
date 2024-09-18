from django.shortcuts import render , redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.contrib.auth import logout # type: ignore
from users.models import Customer
from .serializers import CustomerSerializer,ProfileSerializer
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore 
from rest_framework import permissions, viewsets , mixins # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework import generics # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore

class Regestiration(mixins.CreateModelMixin,  
                   viewsets.GenericViewSet):
    def regster(request):
        
        if request == 'POST':
            serializer = CustomerSerializer
            if serializer.is_valid():
                serializer.save()
                username=serializer.cleaned_data.get('username')
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response({'error': 'No bookings '}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
@permission_classes([IsAuthenticated])    
class Logout(generics.GenericAPIView):
    def logout(request):
        serializer = CustomerSerializer
        logout(request)
        return Response('Logged out!')


@permission_classes([IsAuthenticated])
class Profile(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin) :
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    profile_serializer = ProfileSerializer
    def get_object(self):
        # Retrieve the customer object for the logged-in user
        customer, created = Customer.objects.get_or_create(user=self.request.user, defaults={'email': self.request.user.email})
        return customer

    def update(self, request, *args, **kwargs):
        customer = self.get_object()  # Get the current Customer object
        
        # Deserialize data using the CustomerSerializer
        customer_serializer = CustomerSerializer(instance=customer, data=request.data)
        
        # Deserialize profile image using the ProfileSerializer
        profile_serializer = ProfileSerializer(instance=customer, data=request.data, partial=True)

        if customer_serializer.is_valid() and profile_serializer.is_valid():
            customer_serializer.save()  # Save user-related data
            profile_serializer.save()   # Save profile-related data
            
            return Response({'status': 'Profile updated successfully'})
        else:
            return Response({
                'customer_errors': customer_serializer.errors,
                'profile_errors': profile_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)