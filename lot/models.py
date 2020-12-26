import time
from django.db import models
from mptt import models as mptt_models
from account.models import BaseUser as Account

# Create your models here.

def upload_product_img(instance, filename):
    lastDot = filename.rfind('.')
    extension = filename[lastDot:len(filename):1]
    return 'images/lot/%s-%s-%s' % (instance.slug, time.time(), extension)

class Category(mptt_models.MPTTModel):
    category_name = models.CharField(max_length=255)
    parent = mptt_models.TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=500, unique=True)

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def __str__(self):
        return self.category_name

class Lot(models.Model):
    lot_name = models.CharField(max_length=255)
    lot_description = models.TextField()
    lot_start_price = models.IntegerField()
    lot_image = models.FileField(upload_to=upload_product_img)
    lot_activity = models.BooleanField(default=True)
    lot_start_time = models.DateTimeField()
    categories = mptt_models.TreeManyToManyField(Category, related_name='lots')
    slug = models.SlugField(max_length=500)

    def __str__(self):
        return self.lot_name

class Price(models.Model):
    lots = models.OneToOneField(Lot,on_delete=models.CASCADE)
    step_price = models.IntegerField()
    final_price = models.IntegerField()
    auto_price = models.IntegerField()
    last_owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def click(self, id):
        pass

    def auto(self, id, auto_trade):
        pass

