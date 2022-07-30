from tabnanny import verbose
from django.db import models
from django.utils import timezone

class DollarRate(models.Model):
    date = models.DateField("Yaratilgan vaqti", default=timezone.now)
    rate = models.DecimalField("Kurs", max_digits=10, decimal_places=2, blank=True)

    class Meta:
        verbose_name = "kurs"
        verbose_name_plural = "Dollar kursi"

    def __str__(self) -> str:
        return f"{self.rate} - {self.date}"
