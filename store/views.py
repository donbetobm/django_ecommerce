from django.shortcuts import get_object_or_404, render

# Create your views here.
# Since we're working with models, we need to import them
from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }

# functions are basically the requests
def all_products(request):
    # we run a query, SQL, to return all the products in the products table
    products = Product.objects.all()
    # let's save the data and make sure is available in the template
    # we are returning the template we want to use and the data we need
    return render(request, 'store/home.html', {'products': products})
 
# this function will allow us to make a query to the database collecting the item's name, which will be in the url as well
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product' : product})

# this function will allow us to see a page with the categories, we'll pass the category_slug to be able to make the query we want
def category_list(request, category_slug=None):
    # first we get the object to select one item from the database into Category table with the slug passed as parameter
    category = get_object_or_404(Category, slug=category_slug)
    # Now we can use category variable to make a query in products database: find everything where category is category (variable)
    products = Product.objects.filter(category=category)
    # we return and create a new template
    return render(request, 'store/products/category.html', {'category': category, 'products': products})