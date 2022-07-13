from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
]