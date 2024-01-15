from django.urls import path
from .views import login, register, profile, line_login_callback

app_name = 'student'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/<int:student_id>/', profile, name='profile'),
    path('login/callback/', line_login_callback, name='line_login_callback'),
]