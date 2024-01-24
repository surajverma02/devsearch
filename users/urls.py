from django.urls import path
from users.views import *


urlpatterns = [
    path('', profiles, name="profiles"),
    path('profile/<str:pk>/', userProfile, name="user-profile"),
]
