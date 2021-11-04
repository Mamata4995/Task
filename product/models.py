from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=50, decimal_places=2)
    price = models.DecimalField(max_digits=5000, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    def create(self):
        self.created_at = timezone.now()
        self.save()

    def update(self):
        self.updated_at =timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("product_detail",kwargs={'pk':self.pk})

    def get_absolute_url(self):
        return reverse('product_list')

    def __str__(self):
        return self.name
