from django.db import models
import uuid
from django.utils import timezone
from django.db.models.functions import Lower
# Create your models here.

class Level(models.TextChoices):
    JUNIOR = "JR", "Junior"
    MID = "MID", "Mid"
    SENIOR = "SR", "Senior"
    INTERN = "INTERN", "Intern"

# We use unique constraint to perform multi-level/combinational unique constraint validation. meaning no two combination of title and level should be duplicate in db
class EmployeeRole(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    level = models.CharField(max_length=10, choices=Level.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('title'),
                'level',
                name='unique_role_title_level'
            )
        ]


    def __str__(self):
        return f"{self.level}|{self.title}"

class Employee(models.Model):
    emp_id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False),
    emp_name = models.CharField(max_length=64, null=False, blank=False)
    emp_email = models.EmailField(max_length=120)
    joining_date = models.DateTimeField(default=timezone.now)
    department = models.ForeignKey('Department.Department', on_delete=models.PROTECT)# Interpreted as do not delete department if one or more employee exist there
    role = models.ForeignKey(EmployeeRole,null=True, on_delete=models.SET_NULL ) # Interpreted as if any role is deleted, set the column to null, as an employee can have no role.
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subordinates')
    salary = models.IntegerField(default=7000, null=False, blank=False)

    def __str__(self):
        return self.emp_name
    

class EmployeeProfile(models.Model):
    employee = models.OneToOneField(to=Employee, on_delete=models.CASCADE) # Interpreted as if employee is deleted, delete the profile too
    phone_number = models.CharField(max_length=12, unique=True, null=False, blank=False)
    address = models.CharField(max_length = 65, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.employee.emp_name
    




