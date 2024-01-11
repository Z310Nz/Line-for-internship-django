# company/urls.py
from django.urls import path
from .views import login
from .views import register_company
from .views import line_login_callback
from .views import profile

app_name = 'company'  # Add this line

urlpatterns = [
    path('logincom/', login, name='login'),
    path('registercom/', register_company, name='register_company'),
    path('logincom/callback/', line_login_callback, name='line_login_callback'),
    path('profilecom/', profile, name='profile')
]