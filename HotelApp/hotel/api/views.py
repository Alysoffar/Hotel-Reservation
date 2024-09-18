from django.contrib.auth.models import Group, User # type: ignore
from rest_framework import permissions, viewsets # type: ignore
from hotel.models import Hotel
from .serializers import HotelSerializer
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore

class AboutPage(viewsets.ViewSet):
    def get(self , request):
        data = {
            'title': 'About',
            'Content':'We are a hotel running for 30 years'
        }
        return Response(data , status=status.HTTP_200_OK)
    
class VisionPage(viewsets.ViewSet):
    def get(self , request):
        data = {
            'title': 'Vision',
            'Content':'Our vision is to become the preferred destination for travelers seeking a perfect blend of luxury, comfort, and cultural richness. We aspire to set a new standard in the hospitality industry, where each guest is treated not just as a visitor, but as a part of our extended family. By continuously innovating and enhancing our offerings, we aim to create an unparalleled experience that leaves a lasting impression on every guest. Our goal is to be recognized globally for our commitment to excellence, sustainability, and community involvement, making us not only a place to stay but a destination in itself.'
        }
        return Response(data , status=status.HTTP_200_OK)
    
class MissionPage(viewsets.ViewSet):
    def get(self , request):
        data = {
            'title': 'Mission',
            'Content':'Our mission is to provide an extraordinary hospitality experience by combining world-class amenities with personalized service that anticipates the needs of every guest. We are dedicated to creating a welcoming and comfortable environment where guests can relax, rejuvenate, and enjoy the finer things in life. Our team is committed to going above and beyond to ensure that every detail of your stay is perfect, from the moment you check in to the time you leave. We strive to create memorable moments that reflect the essence of our brand – warmth, elegance, and unmatched service'
        }
        return Response(data , status=status.HTTP_200_OK)   
    
class ApproachPage(viewsets.ViewSet):
    def get(self , request):
        data = {
            'title': 'Approach',
            'Content':'Our approach is centered around the belief that every guest deserves a unique and tailored experience. We focus on understanding the diverse needs of our guests and delivering solutions that exceed their expectations. We invest in continuous training for our staff to ensure they provide top-notch service with a personal touch. Sustainability is at the core of our operations, and we actively seek ways to minimize our environmental impact while supporting local communities. By fostering a culture of innovation and teamwork, we ensure that every aspect of our hotel, from design to service, reflects our commitment to excellence and guest satisfaction..'
        }
        return Response(data , status=status.HTTP_200_OK)       

class HomePageViewSet(viewsets.ModelViewSet):
    querysets=Hotel.objects.all()
    serializer = HotelSerializer
