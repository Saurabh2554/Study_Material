"""
We register a model with Django Admin to expose it in the admin interface for CRUD operations.
If we do not register it, the model still exists in the database and works normally, but it will not be visible or manageable through the admin UI.
Django requires explicit registration to maintain security, control, and customization over which models are exposed.
"""


from django.contrib import admin
from .models import Employee, EmployeeProfile, EmployeeRole
# Register your models here.

# Customization before exposing the model/model-fields to admin web interface. For detailed description ref: /Users/sranja/Library/CloudStorage/OneDrive-DataAxle/Documents/github/Microservices/Microservices/Ecommerce_Modular_Monolithic/Django_Concepts/admin.md


# Below are the example of classic style model and respective Admin model registeration:
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'emp_name', 'emp_email', 'joining_date']
    search_fields = ('emp_name', 'emp_email') #searching allowed by name and email only

admin.site.register(Employee, EmployeeAdmin)

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'address']
    search_fields = ('phone_number','address')

admin.site.register(EmployeeRole)    

"""
#But we can also use decorator pattern to register model and it's admin at once

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']
    search_fields = ('name', 'email') #searching allowed by name and email only

Here:
    1. Django sees the class EmployeeAdmin
    2. The decorator is applied to that class
    3. The decorator internally calls: admin.site.register(Employee, EmployeeAdmin)
"""

