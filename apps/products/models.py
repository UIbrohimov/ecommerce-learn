from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Result(models.Model):
  title = models.CharField('Product',max_length=255)
  category = TreeForeignKey('Group',null=True,blank=True,on_delete=models.CASCADE)
  price = models.CharField('Price', max_length=255)
  content = models.TextField('Information')
  image = models.ImageField('Image')
  rate = models.IntegerField('Rate')
  cash = models.BooleanField('Cash')
  card = models.BooleanField('Card')
  active = models.BooleanField('Active')
  slug = models.SlugField('Slug', max_length=255, default=title)

  class Meta:
    verbose_name = 'product'
    verbose_name_plural = 'products'

  def __str__(self):
    return self.title

    
class Group(MPTTModel):
  name = models.CharField(max_length=255, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
  slug = models.SlugField(max_length=255, default=name)

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name
