from django.db import models
import uuid
# Create your models here.

class Department(models.Model):
    dept_id = models.UUIDField(
       default=uuid.uuid4,
       editable=False
    ),
    dept_name = models.CharField(max_length=50, unique=True)
    dept_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.dept_name   
