from django.db import models


class About(models.Model):

    title = models.CharField("Sarlavha", max_length=255)
    content = models.TextField("Asosiy qism")

    class Meta:
        verbose_name = "content"
        verbose_name_plural = "contents"
