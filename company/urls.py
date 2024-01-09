# company/urls.py
from django.urls import path
from .views import login
from .views import register

app_name = 'company'  # Add this line

urlpatterns = [
    path('logincom/', login, name='login'),
    # Add other URLs as needed
    path('registercom/', register, name="register"),
]
