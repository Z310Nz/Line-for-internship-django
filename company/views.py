from django.shortcuts import render

# Create your views here.
def login(request):
    # Your login view logic goes here
    return render(request, 'company/login.html')