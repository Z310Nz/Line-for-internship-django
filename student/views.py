# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from .forms import StudentForm
from django.urls import reverse
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

# Import LIFF SDK
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

line_bot_api = LineBotApi('bPGIDybNuOJyZ2vo6+25vHTQ5Olq9Hg1HtTqxvPR1vE7CJOALaUVH98BK/LFwiSa0HLJdKo+UZkdmDoHbtFquvmLbDYO0kFGQA3WCx7XtxqnOHpJHxtD96qBxLjldbI09zGYEotbIA7DS1LM6U5sLAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0b1cbba3a5d2b14e4db1c53ac899d1bf')

def line_login_callback(request):
    # user = authenticate(request, line_id=request.GET.get('id_line'))
    user = 

    if user is not None and user.is_student:
        login(request, user)
        return redirect('student:profile', student_id=user.student.id)
    elif user is not None and user.is_company:
        login(request, user)
        return redirect('company:profile', company_id=user.company.id)
    else:
        return redirect('student:register')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        if 'user_role' in request.session:
            role = request.session['user_role']
            return redirect('student:profile') if role == 'student' else redirect('company:profile')
        else:
            return redirect('student:register')
    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            return redirect('student:profile', student_id=student.id)
    else:
        form = StudentForm()

    return render(request, 'registerstd.html', {'form': form})


def profile(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'profile.html', {'student': student})
