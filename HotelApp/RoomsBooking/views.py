from django.shortcuts import render, get_object_or_404 , reverse ,redirect# type: ignore
from .models import UserRegistration , Room 
from users.models import Customer
from .forms import UserBookingForm # type: ignore
from django.contrib import messages # type: ignore
from django.core.exceptions import ObjectDoesNotExist # type: ignore
from django.utils import timezone # type: ignore
from django.http import HttpResponse , HttpResponseRedirect # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # type: ignore
from django.views.generic import DeleteView,UpdateView # type: ignore


def room(request):
    rooms = Room.objects.all()
    return render(request, 'RoomsBooking/rooms.html', {'rooms': rooms})

def book(request, room_id):
    if request.method == "POST":
        form = UserBookingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['startdate']
            end_date = form.cleaned_data['enddate']
            room = get_object_or_404(Room, id=room_id)
            try:
                customer = get_object_or_404(Customer, user=request.user)
            except ObjectDoesNotExist:
                messages.error(request, "You need to complete your profile before booking.")
                return redirect('register')
            
            is_available =  not UserRegistration.objects.filter(
                room=room,
                startdate__lt=end_date,
                enddate__gt=start_date
            ).exists()

            if is_available:
                booking = form.save(commit=False)
                booking.customer = request.user.customer
                booking.room = room
                booking.save()
                messages.success(request, 'Your booking has been created!')
                return redirect('rooms')  
            else:
                messages.error(request, 'The room is not available for the selected dates.')
                return redirect('booking_page', room_id=room_id)
        else:
            messages.error(request, 'Invalid form data. Please correct the errors below.')
    else:
        form = UserBookingForm(initial={'room_id': room_id})

    return render(request, 'RoomsBooking/booking.html', {'form': form, 'room_id': room_id})


@login_required
def user_bookings(request):
    user = get_object_or_404(Customer, user=request.user)
    bookings = UserRegistration.objects.filter(customer=user).order_by('-id')
    
    if not bookings:
        messages.warning(request, "No bookings found.")
    
    return render(request, 'RoomsBooking/booking_user_view.html', {'bookings': bookings , 'room':room})



class BookingUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserRegistration
    fields = ['startdate', 'enddate']
    template_name = 'RoomsBooking/booking_update.html'
    success_url = reverse_lazy('booking_view')  # Redirect after successful update

    def form_valid(self, form):
        form.instance.startdate = self.request.POST.get('startdate')
        form.instance.enddate = self.request.POST.get('enddate')
        return super().form_valid(form)
    
    def test_func(self):
        # Only allow users to edit their own bookings
        booking = self.get_object()
        return self.request.user.customer == booking.customer

    def get_queryset(self):
        """Filter bookings to ensure users can only see their own bookings"""
        qs = super().get_queryset()
        return qs.filter(customer=self.request.user.customer)



class BookingCancelView(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
    model = UserRegistration
    success_url = reverse_lazy('booking_view')  #
    template_name = 'RoomsBooking/booking_delete.html'
    def test_func(self) -> bool:
        booking = self.get_object()
        if self.request.user == booking.customer.user:
            return True
        return False
