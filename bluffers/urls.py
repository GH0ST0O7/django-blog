from django.urls import path
from .views import UserRegistrationView
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name="register"),

    path('login/', LoginView.as_view(),name= "login"),


]