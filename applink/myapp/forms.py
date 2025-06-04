from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'position', 'hire_date', 'is_active']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
            'is_active': forms.CheckboxInput(),
        }
        Labels = {
            'first_name': "First Name",
            'Last_name': "Last Name",
            'email': "Email Address",
            'position': "Position",
            'hire_date': "Hire Date",
            'is_active': "Active status",
        }