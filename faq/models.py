from django.db import models
from common.enums import STATUS, Status
from common.models import DateTimeLog


# Create your models here.
class FAQ(DateTimeLog):
    question = models.CharField(max_length=1000)
    answer = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS, default=Status.ACTIVE)

    def __str__(self):
        return self.question
