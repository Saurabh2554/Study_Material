from django import forms
from .models import Employee, EmployeeProfile
from datetime import date
from django.core.exceptions import ValidationError

class EmployeeForms(forms.ModelForm):
    def clean_esal(self):
        inputsal = self.cleaned_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('The minm salary should be 5000.')
        return inputsal
    
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeProfileForm(forms.ModelForm):
    def clean_date_of_birth(self):
        dob = self.cleaned_data.get("date_of_birth")

        if dob is None:
            return dob

        today = date.today()
        age = (
            today.year
            - dob.year
            - ((today.month, today.day) < (dob.month, dob.day))
        )
        if age < 18:
            raise ValidationError("Employee must be at least 18 years old.")
        return dob

    class Meta:
        model = EmployeeProfile
        exclude = ("employee",)

        