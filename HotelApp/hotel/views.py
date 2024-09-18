from django.shortcuts import render # type: ignore
from django.views.generic import DetailView # type: ignore
from .models import Hotel

    
    

def home(request):
    context ={
        'hotels':Hotel.objects.all()
    }
    return render(request , 'hotel/home.html',context)

def about(request):
    return render(request, 'hotel/about.html')

def booking(request):
    return render(request, 'hotel/booking.html')

def vision(request):
    return render(request, 'hotel/vision.html')

def mission(request):
    return render(request, 'hotel/mission.html')

def approach(request):
    return render(request, 'hotel/approach.html')