from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=255, blank=True)
    email2 = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    phone2 = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.email

from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
