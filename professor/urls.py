# professor/urls.py
from django.urls import path
from .views import login

app_name = 'professor'  # Add this line

urlpatterns = [
    path('login/', login, name='login'),
    # Add other URLs as needed
]
