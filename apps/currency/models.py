from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.
class DollarRate(models.Model):
    date = models.DateField("Yaratilgan vaqti", default=timezone.now)
    rate = models.DecimalField("Kurs", decimal_places=2, max_digits=10, blank=True)

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Dollar kursi"

    def __str__(self) -> str:
        return f"{self.rate} - {self.date}"    