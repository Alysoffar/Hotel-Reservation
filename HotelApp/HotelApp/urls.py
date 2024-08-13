from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from users import views as user_views
from django.contrib.auth import views as auth_views # type: ignore
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('register/',user_views.register , name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('profile/', user_views.profile, name='profile'),
]