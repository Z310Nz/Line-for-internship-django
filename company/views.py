from django.shortcuts import render, redirect
from .forms import CompanyForm, JobForm

# Create your views here.
def login(request):
    # Your login view logic goes here
    return render(request, 'logincom.html')

def register_company(request):
    if request.method == 'POST':
        company_form = CompanyForm(request.POST)
        job_form = JobForm(request.POST)  # สร้าง JobForm ขึ้นมา (ต้องให้ได้ JobForm ในที่นี้)
        if company_form.is_valid() and job_form.is_valid():
            company = company_form.save()
            job = job_form.save(commit=False)
            job.company = company  # กำหนดบริษัทให้กับ Job
            job.save()
            return redirect('success_page')
    else:
        company_form = CompanyForm()
        job_form = JobForm()  # สร้าง JobForm ขึ้นมา (ต้องให้ได้ JobForm ในที่นี้)

    return render(request, 'registercom.html', {'company_form': company_form, 'job_form': job_form})

def profile(request):
    # Your profile view logic goes here
    return render(request, 'profilecom.html')