from django.shortcuts import get_object_or_404 # type: ignore
from RoomsBooking.models import UserRegistration , Room 
from users.models import Customer
from django.contrib import messages # type: ignore
from django.core.exceptions import ObjectDoesNotExist # type: ignore
from django.utils import timezone # type: ignore
from django.http import HttpResponse , HttpResponseRedirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # type: ignore
from django.views.generic import DeleteView,UpdateView # type: ignore
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status  # type: ignore
from rest_framework import permissions, viewsets , mixins# type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework.decorators import action # type: ignore
from .serializers import RoomSerializer , BookingSerializer
from rest_framework.exceptions import PermissionDenied # type: ignore
from rest_framework import viewsets, status # type: ignore
from rest_framework.serializers import ValidationError # type: ignore


class RoomViewset(viewsets.ModelViewSet):
         queryset= Room.objects.all()
         serializer = RoomSerializer



class BookingViewset(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = BookingSerializer 
    lookup_field = 'id'  # Use explicit lookup field for clarity

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
  # Raise validation errors

        # Extract validated data
        validated_data = serializer.validated_data

        try:
            self.validate_booking_data(validated_data)  # Call separate validation function
            booking = self.perform_create(validated_data)  # Separate logic for creating booking
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_404_NOT_FOUND) 


    def validate_booking_data(self, data,**kwargs):
        """Performs additional validation beyond the serializer's scope."""
        start_date = data['startdate']
        end_date = data['enddate']
        room_id = kwargs.get('room_id')

        room = get_object_or_404(Room, pk=room_id)
        overlapping_bookings = UserRegistration.objects.filter(
            room=room,
            startdate__lt=end_date,
            enddate__gt=start_date
        ).exists()

        if overlapping_bookings:
            raise ValidationError({'error': 'Room is not available for the selected dates.'})

    def perform_create(self, validated_data):
        """Creates a new booking instance, assigning customer and room."""
        booking = UserRegistration.objects.create(
            customer=self.request.user.customer,
            room=validated_data['room'],
            **validated_data  # Unpack other validated data
        )
        return booking

class UserBookingset(mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
        def BookingView(request):
                serializer= BookingSerializer
                data = serializer.data
                user = get_object_or_404(Customer, user=request.user)
                bookings = UserRegistration.objects.filter(customer=user).order_by('-id')
                if not bookings:
                        return Response({'error': 'No bookings '}, status=status.HTTP_400_BAD_REQUEST)
                return Response(data, status=status.HTTP_201_CREATED)

class BookingUpdateViewset(mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
        
        def get_queryset(self):
                qs = super().get_queryset()
                return qs.filter(customer=self.request.user.customer)

        def update(self, request, *args, **kwargs):
                instance = self.get_object()
                if instance.customer != request.user.customer:
                        raise PermissionDenied("You do not have permission to edit this booking.")

                return super().update(request, *args, **kwargs)
        
class BookingDeleteset(viewsets.GenericViewSet,
                   mixins.DestroyModelMixin):
        
        def test_func(self) -> bool:
                booking = self.get_object()
                if self.request.user == booking.customer.user:
                        return True
                return False
