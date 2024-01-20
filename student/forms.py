from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'intern_start': forms.DateInput(attrs={'type': 'date'}),
            'intern_end': forms.DateInput(attrs={'type': 'date'}),
            # Add more widgets as needed
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Your custom email validation logic here
        return email
