from django.db import models

# Create your models here.
from common.models import DateTimeLog


class Design(DateTimeLog):

    banner = models.ImageField(upload_to="atarctic-banner", blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    footer = models.TextField(null=True, blank=True)
    mission = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.banner.url
