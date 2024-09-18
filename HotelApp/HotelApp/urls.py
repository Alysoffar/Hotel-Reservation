from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from django.contrib.auth import views as auth_views # type: ignore
from django.views import i18n # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('', include('RoomsBooking.urls')),
    path('', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    
]
