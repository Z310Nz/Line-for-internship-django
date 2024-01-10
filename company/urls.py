# company/urls.py
from django.urls import path
from .views import login
from .views import register_company

app_name = 'company'  # Add this line

urlpatterns = [
    path('logincom/', login, name='login'),
    path('registercom/', register_company, name='register_company'),
]