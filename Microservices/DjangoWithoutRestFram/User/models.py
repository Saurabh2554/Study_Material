from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
# Create your models here.

#In this project i already have an Employee model and now i have a User model. for the first time it seems like duplication of model, but actually it's not as both server different business purpose. User will contain fields like username, email, password, etc, whereas Employee will have a OneToOne field relation with User and will store fields like Department, salary, start_date, EmployeeProfile etc. Technically all Employee will be directly an User but all user may not be an Employee.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    



