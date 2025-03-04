from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [

    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login_obtain_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
