from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Product(models.Model):
    nomi = models.CharField("Mahsulot nomi", max_length=255)
    narxi = models.CharField("Narxi", max_length=255)
    tavsifi = models.TextField("Tavsifi", max_length=255)
    rasmi = models.ImageField("Rasmi", upload_to = "products/", blank=True, null=True)
    baho = models.IntegerField("Baho", validators=[MinValueValidator(0), MaxValueValidator(5)])
    naxt = models.BooleanField("Naqt pul")
    karta = models.BooleanField("Karta orqali")
    active = models.BooleanField("Aktiv")

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
    
    def __str__(self):
        return self.nomi


class Category(models.Model):
    category = models.ForeignKey(
        Product,
        verbose_name="Mahsulot turi",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    

    def __str__(self):
        return self

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"