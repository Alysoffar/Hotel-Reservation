from django.urls import path,include # type: ignore
from . import views
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
urlpatterns = [
    path('api/hotel/', include('hotel.api.urls')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bookin2/', views.booking, name='bookin2'),
    path('vision/', views.vision, name='vision'),
    path('mission/', views.mission, name='mission'),
    path('approach/', views.approach, name='approach'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

