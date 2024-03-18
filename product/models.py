from django.db import models


from common.enums import STATUS, Status
from common.models import DateTimeLog


class Product(DateTimeLog):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS, default=Status.ACTIVE)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    background_video = models.FileField(null=True, blank=True)
    index = models.IntegerField(default=0, null=True, blank=True)
    is_display = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not Product.objects.filter(id=self.id).exists() and Product.objects.all().exists():
            self.index = Product.objects.last().index + 1

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductMedia(DateTimeLog):

    media = models.FileField(upload_to='product-media', blank=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)

