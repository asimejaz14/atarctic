from django.db import models
from common.enums import STATUS, Status
from common.models import DateTimeLog


class User(DateTimeLog):
    username = models.CharField(max_length=128, null=True, blank=True)
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=1, choices=STATUS, default=Status.ACTIVE)
    is_restricted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
