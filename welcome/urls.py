from django.urls import path
from .views import welcome_page

app_name = 'welcome'

urlpatterns = [
    path('', welcome_page, name='welcome_page'),
]