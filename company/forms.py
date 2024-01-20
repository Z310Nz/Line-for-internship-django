# forms.py
from django import forms
from .models import Company, Job

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'foundation_date': forms.DateInput(attrs={'type': 'date'}),
            # Add more widgets as needed
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = {
            'workstart': forms.TimeInput(attrs={'type': 'time'}),
            'workend': forms.TimeInput(attrs={'type': 'time'}),
            # Add more widgets as needed
        }

    def clean_email(self):
        # Add custom validation for the email field if needed
        email = self.cleaned_data.get('email')
        # Your validation logic here
        return email
