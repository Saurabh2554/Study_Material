from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=60,unique=True, null=False, blank = False)
    start_date = models.DateField(auto_now_add=True ,blank=False, null=False)
    end_date = models.DateField(auto_now_add=True,blank=True, null=True)
    is_Active = models.BooleanField(blank=False, null=False)
    asignee = models.ManyToManyField(to='testApp.Employee',related_name="projects")


    def __str__(self):
        return self.name