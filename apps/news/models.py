from django.urls import reverse
from django.utils import timezone
from django.db import models


class Post(models.Model):
    title = models.CharField("Sarlavha", max_length=255)
    slug = models.SlugField("Slag", max_length=268, unique=True)
    discription = models.TextField("Qisqacha tavsif", blank=True)
    content = models.TextField("Kontent")
    image = models.ImageField("Rasm", upload_to="yangilikar/")
    published = models.DateField("Chop etilgan sana", default=timezone.now)

    class Meta:
        verbose_name = "yangilik"
        verbose_name_plural = "Yangiliklar"
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("news:detail", kwargs={"slug": self.slug})
