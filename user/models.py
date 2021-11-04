from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=10, blank=False)
    last_name = models.CharField(max_length=10, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=20,blank=False)
    username = models.CharField(max_length=15,blank=False)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    def create(self):
        self.created_at = timezone.now()
        self.save()

    def update(self):
        self.updated_at =timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
