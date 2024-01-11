from django.shortcuts import render, redirect
from .forms import CompanyForm, JobForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

# Create your views here.\
def line_login_callback(request):
    user = authenticate(request, line_id=request.GET.get('line_id'))
    
    if user is not None and user.is_company:
        login(request, user)
        return redirect('company:profile', company_id=user.company.id)
    elif user is not None and user.is_student:
        # Redirect to the appropriate page for the student role
        return redirect('student:profile', student_id=user.student.id)
    else:
        return redirect('company:register_company')


    
def login(request):
    return render(request, 'logincom.html')

def register_company(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        job_form = JobForm(request.POST)
        if company_form.is_valid() and job_form.is_valid():
            company = company_form.save()
            job = job_form.save(commit=False)
            job.company = company
            job.save()

            # Authenticate the user and login
            user = authenticate(request, line_id=company.line_id)
            if user is not None and user.is_company:
                login(request, user)
                return redirect('company:profile')
                
    else:
        company_form = CompanyForm()
        job_form = JobForm()

    return render(request, 'registercom.html', {'company_form': company_form, 'job_form': job_form})

@login_required
def profile(request):
    # Assuming you have a custom User model for the Company
    company = request.user.company
    
    # Assuming you have a model named 'Job' related to the Company model
    jobs = company.job_set.all()

    # You can add other data retrieval logic here based on your models
    
    context = {
        'company': company,
        'jobs': jobs,
        # Add other data to the context as needed
    }

    return render(request, 'profilecom.html', context)