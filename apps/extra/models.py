from django.db import models


class ImgCategory(models.Model):
    name = models.CharField("Kategoriya", max_length=255)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Rasm kategoriyalari"

    def __str__(self) -> str:
        return self.name


class Gallery(models.Model):
    category = models.ForeignKey(
        ImgCategory,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    title = models.CharField("nomi", max_length=255, blank=True)
    image = models.ImageField("rasm", upload_to="images/")

    class Meta:
        ordering = ('id',)
        verbose_name = "rasm"
        verbose_name_plural = "Rasmlar"

    def __str__(self) -> str:
        return f"{self.id} - rasm"