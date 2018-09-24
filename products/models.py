from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    tag = TaggableManager()
    
    def __str__(self):
        return self.name
    
    
# class PostPicture(models.Model):
#     image = models.ImageField(upload_to='images')
#     productid = models.ForeignKey('Product')
    
# class Product(models.Model):
#     name = models.CharField(max_length=254, default='')
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     # userid = models.ForeignKey(admin, related_name='userblogpost')
#     # Picture = None



    
    
#     def __str__(self):
#         return self.name
        

        
