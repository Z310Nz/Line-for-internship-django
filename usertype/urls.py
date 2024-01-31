# usertype/urls.py

from django.urls import path, include
from . import views
from .views import company_register

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', include('usertype.student_urls')),
    path('company/', include('usertype.company_urls')),
    path('professor/', views.professor_dashboard, name='professor_dashboard'),
    path('company/register/', company_register, name='register_company'),
    path('company/login/', views.company_login, name='login_company'),
    path('student/register/', views.student_register, name='register_student'),
    path('student/login/', views.student_login, name='login_student'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('company/profile/', views.company_profile, name='company_profile'),
    path('student/edit_profile/', views.student_edit_profile, name='student_edit_profile'),
    path('company/edit_profile/', views.company_edit_profile, name='company_edit_profile'),
    path('company/add_position/', views.add_position, name='add_position'),
    path('professor/add_position/', views.add_position, name='add_position'),
]
