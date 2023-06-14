from django.db import models

from common.models import DateTimeLog


# Create your models here.
class Inquiry(DateTimeLog):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    message = models.CharField(max_length=200, null=True, blank=True)
    assigned_to = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
