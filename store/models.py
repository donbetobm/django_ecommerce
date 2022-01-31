from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

from core.settings import AUTH_PASSWORD_VALIDATORS


# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    # slugfield verifies that there are not special characters being sending to the database
    # slug variable will allow us to make sure that the database stores uniques categories only
    slug = models.SlugField(max_length=255, unique=True)
    
    # A class within a class for setting a plural name for each category
    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])
    

    """
    Data will be returned data from the database. By default we return the data which has two components
    in this case: name and slug, and other components that might be added as well.
    We need to refer that data that is return, and we need a method in order to do that. 
    That's why we return 'self.name' in the following def '__str__' function
    """
    def __str__(self):
        return self.name


class Product(models.Model):
    # this is a relationship created within product and category; this allows us to have information
    # from another table within this one. It's a reference.
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    tittle = models.CharField(max_length=255)
    author = models.TextField(blank=True, default='admin')
    description = models.TextField(blank=True)
    # this allows to handle images processing, it doesn't store the images in the database, refers the link
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    # Default product manager
    objects = models.Manager()
    # New product manager
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    

    
    def __str__(self):
        return self.tittle