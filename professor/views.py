# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from student.models import Student
from company.models import Company
from django.contrib import messages
from .forms import ProfessorLoginForm
from .decorators import logout_required

@logout_required
def login_view(request):
    if request.method == 'POST':
        form = ProfessorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('professor:dashboard')  # Redirect to the dashboard page
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = ProfessorLoginForm()

    return render(request, 'loginpfs.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('professor:login')

@login_required
def dashboard(request):
    student_count = Student.objects.count()
    company_count = Company.objects.count()

    context = {
        'student_count': student_count,
        'company_count': company_count,
        'user': request.user,  # Assuming you are using the default User model
    }

    return render(request, 'dashboard.html', context)
