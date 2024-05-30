from django.db import models
from django.db.models import Model
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", 
                             on_delete=models.PROTECT,
                             null=True,
                             blank=True)
    
    class MPTTMeta:
        order_insertionm_by = ['name']
    
    def __str__(self) -> str:
        return f"Category: {self.name}"
    

class Brand(Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Brand: {self.name}"

class Product(Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE)
    category = TreeForeignKey('Category', 
                              null=True,
                              blank=True,
                              on_delete=models.SET_NULL)
    
    
    def __str__(self) -> str:
        return f"Product: {self.name}"