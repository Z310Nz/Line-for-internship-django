from django.shortcuts import render

# Create your views here.
def login(request):
    # Your login view logic goes here
    return render(request, 'logincom.html')

def register(request):
    # Your register view logic goes here
    return render(request, 'registercom.html')

def profile(request):
    # Your profile view logic goes here
    return render(request, 'profilecom.html')