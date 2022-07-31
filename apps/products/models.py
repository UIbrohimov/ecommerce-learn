from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class ChoicePayment(models.IntegerChoices):
    NONE = 0, 'None'
    CASH = 1, 'Cash'
    CARD = 2, 'Card'


class Product(models.Model):
  title = models.CharField('Product',max_length=255)
  # category = TreeForeignKey('Group',null=True,blank=True,on_delete=models.CASCADE)
  cat = models.ForeignKey(
    'Category',
    on_delete=models.SET_NULL,
    blank=True,
    null=True,
    related_name="products"
  )
  price = models.CharField('Price', max_length=255)
  content = models.TextField('Information')
  image = models.ImageField('Image')
  rate = models.IntegerField('Rate')
  payment = models.IntegerField('Payment', default=ChoicePayment.NONE, choices=ChoicePayment.choices)
  active = models.BooleanField('Active')
  slug = models.SlugField('Slug', max_length=255, unique=True)

  class Meta:
    verbose_name = 'product'
    verbose_name_plural = 'products'

  def str(self):
    return self.title

    
class Category(MPTTModel):
  name = models.CharField(max_length=255, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
  slug = models.SlugField('Slug', max_length=255, unique=True)

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def str(self):
    return self.name