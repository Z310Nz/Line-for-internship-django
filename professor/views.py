from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def login(request):
    # Your login view logic goes here
    return render(request, 'professor/login.html')
def dashboard(request):
    # Your dashboard logic here
    return render(request, 'professor/dashboard.html')