from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import HomePageViewSet , ApproachPage,MissionPage ,VisionPage ,AboutPage

router = DefaultRouter()
router.register(r'hotels', HomePageViewSet , basename='hotel')
router.register(r'mission', MissionPage , basename='mission')
router.register(r'vision', VisionPage , basename='vision')
router.register(r'approach', ApproachPage , basename='approach')
router.register(r'about', AboutPage , basename='about')

urlpatterns = [
     
]+router.urls
