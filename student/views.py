# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Student app views.py
def line_login_callback(request):
    user = authenticate(request, line_id=request.GET.get('line_id'))
    
    if user is not None and user.is_student:
        login(request, user)
        return redirect('student:profile', student_id=user.student.id)
    elif user is not None and user.is_company:
        # Redirect to the appropriate page for the company role
        return redirect('company:profile', company_id=user.company.id)
    else:
        return redirect('student:register')


def login(request):
    # Your LINE login implementation using LIFF
    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('profile', student_id=student.id)  # Pass student_id as a parameter
    else:
        form = StudentForm()

    return render(request, 'registerstd.html', {'form': form})


@login_required
def profile(request, student_id):
    student = Student.objects.get(id=student_id)  # Retrieve the student using the provided student_id
    # Your profile logic here
    return render(request, 'profile.html', {'student': student})
