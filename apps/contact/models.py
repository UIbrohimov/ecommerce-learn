from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.EmailField(max_length=255, blank=True)
    email2 = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    phone2 = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email

from django.db import models


class ContactView(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
