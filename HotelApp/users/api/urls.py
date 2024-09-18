from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import Regestiration,Logout,Profile
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'register', Regestiration, basename='register')
router.register(r'profile', Profile, basename='profile')

urlpatterns = [
     path('logout/',Logout.as_view(),name='logout'),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+router.urls
