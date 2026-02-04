from django.forms import ModelForm
from .models import Department

class DepartmentForms(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"