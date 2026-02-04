from django.contrib import admin
from .models import Department
# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id','dept_name','dept_code']
    search_fields = ['dept_name','dept_code']

