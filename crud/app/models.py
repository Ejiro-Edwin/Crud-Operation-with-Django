from django.db import models
from datetime import datetime

# Create your models here.

class crud(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name
    class Meta:
        verbose_name_plural = "crud"