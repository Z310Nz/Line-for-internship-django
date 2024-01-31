# forms.py

from django import forms
from django.contrib.auth import authenticate
from .models import Student, Company, Professor
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class BaseLineLoginForm(forms.Form):
    line_user_info = None
    user_type = None

    def clean(self):
        cleaned_data = super().clean()
        self.user = authenticate(self.request, line_user_info=self.line_user_info, user_type=self.user_type)
        if not self.user:
            raise forms.ValidationError("Invalid Line login.")
        return cleaned_data

class StudentLoginForm(BaseLineLoginForm):
    user_type = 'student'

class CompanyLoginForm(BaseLineLoginForm):
    user_type = 'company'

class ProfessorLoginForm(BaseLineLoginForm):
    user_type = 'professor'

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Student  # Use the Student model
        fields = ['username', 'email', 'password1', 'password2', 'student_id', 'profile_image', 'sfirst_name', 'slast_name', 'nick_name', 'birthdate', 'gender', 'semail', 'phone_number', 'line_id', 'website', 'cv', 'last_job', 'skills', 'education', 'date_intern']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'student_id': 'Student ID',
            'profile_image': 'Profile Image',
            'sfirst_name': 'First Name',
            'slast_name': 'Last Name',
            'nick_name': 'Nick Name',
            'birthdate': 'Birthdate',
            'gender': 'Gender',
            'semail': 'Email',
            'phone_number': 'Phone Number',
            'line_id': 'Line ID',
            'website': 'Website',
            'cv': 'CV',
            'last_job': 'Last Job',
            'skills': 'Skills',
            'education': 'Education',
            'date_intern': 'Date Intern',
        }
class CompanyRegistrationForm(UserCreationForm):
    class Meta:
        model = Company
        fields = ['username', 'email', 'password1', 'password2', 'company_name', 'profile_image', 'company_description', 'Foundation_date', 'Company_type', 'number_employee', 'website', 'cemail', 'Address', 'add_job']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'company_name': 'Company Name',
            'profile_image': 'Profile Image',
            'company_description': 'Company Description',
            'Foundation_date': 'Foundation Date',
            'Company_type': 'Company Type',
            'number_employee': 'Number of Employees',
            'website': 'Website',
            'cemail': 'Email',
            'Address': 'Address',
            'add_job': 'Add Job',
        }