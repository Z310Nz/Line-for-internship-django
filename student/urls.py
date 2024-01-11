from django.urls import path
from .views import login
from .views import register

app_name = 'student'

urlpatterns = [
    path('login/', login, name='login'),
    path('registerstd/', register, name='register'),
    # path('profile/', profile, name='profile'),
    # Add other URLs as needed
]