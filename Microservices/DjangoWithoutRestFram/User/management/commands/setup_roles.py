from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from testApp.models import Employee
from Department.models import Department

class Command(BaseCommand):
    help = 'Create roles/groups and assign permissions'

    def handle(self, *args, **kwargs):
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        manager_group, _ = Group.objects.get_or_create(name='Manager')
        employee_group, _ = Group.objects.get_or_create(name='Employee')

        content_type = ContentType.objects.get_for_model(Employee)

        # creating permissions for employee
        view_emp, _ = Permission.objects.get_or_create(codename='view_employee',content_type=content_type)
        add_emp, _ = Permission.objects.get_or_create(codename='add_employee', content_type=content_type)
        change_emp, _ = Permission.objects.get_or_create(codename='change_employee', content_type=content_type)
        delete_emp, _ = Permission.objects.get_or_create(codename='delete_employee', content_type=content_type)

        content_type_dept = ContentType.objects.get_for_model(Department)

        view_dept, _ = Permission.objects.get_or_create(codename='view_department', content_type=content_type_dept)
        add_dept, _ = Permission.objects.get_or_create(codename='add_department', content_type=content_type_dept)
        # change_dept = Permission.objects.get_or_create(codename='change_department', content_type=content_type_dept)
        # delete_dept = Permission.objects.get_or_create(codename='delete_department', content_type=content_type_dept)

         #Adding permissions to group
        admin_group.permissions.set([view_emp, add_emp, change_emp, delete_emp, view_dept, add_dept, change_emp])
        manager_group.permissions.set([view_emp, change_emp, view_dept])
        employee_group.permissions.set([view_emp])

        self.stdout.write(self.style.SUCCESS('Roles and permissions have been set up successfully!'))










