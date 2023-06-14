from django.db import models

from common.models import DateTimeLog


# Create your models here.
class Partner(DateTimeLog):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='AtArctic/partners/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not Partner.objects.filter(id=self.id).exists() and Partner.objects.all().exists():
            self.index = Partner.objects.last().index + 1

        super(Partner, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

