from django.db import models

# Create your models here.



class Product(models.Model):
    name  = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

    def __str__(self):         
        return self.name


class Shop(models.Model):
    name  = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    address  = models.CharField(max_length=30)
    zip_code  = models.CharField(max_length=30)
    city  = models.CharField(max_length=30)
    state  = models.CharField(max_length=30)
    country  = models.CharField(max_length=30)
    products = models.ManyToManyField(Product)

    def __str__(self):         
        return self.name
    

class Item(models.Model):
    name  = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    image = models.ImageField('Item', upload_to='upload/')
    product =  models.ForeignKey(Product)
    shop  = models.ForeignKey(Shop)
    def __str__(self):         
        return self.name
