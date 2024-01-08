from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student

# Create your views here.
def login(request):
    # Your LINE login implementation using LIFF
    return render(request, 'login.html')

def register(request):
    # Your registration logic here
    return render(request, 'register.html')

@login_required
def profile(request):
    # Your profile logic here
    return render(request, 'profile.html')
