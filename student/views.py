from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

def login(request):
    # Your LINE login implementation using LIFF
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful submission
    else:
        form = StudentForm()

    return render(request, 'registerstd.html', {'form': form})


@login_required
def profile(request):
    # Your profile logic here
    return render(request, 'profile.html')
