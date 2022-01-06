from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    # slugfield verifies that there are not special characters being sending to the database
    # slug variable will allow us to make sure that the database stores uniques categories only
    slug = models.SlugField(max_length=255, unique=True)
    
    # A class within a class for setting a plural name for each category
    class Meta:
        verbose_name_plural = 'categories'

    """
    Data will be returned data from the database. By default we return the data which has two components
    in this case: name and slug, and other components that might be added as well.
    We need to refer that data that is return, and we need a method in order to do that. 
    That's why we return 'self.name' in the following def '__str__' function
    """
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    # this is a relationship created within product and category; this allows us to have information
    # from another table within this one. It's a reference.
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)