from django.shortcuts import render

# Create your views here.
# Since we're working with models, we need to import them
from .models import Category, Product

# functions are basically the requests
def all_products(request):
    # we run a query, SQL, to return all the products in the products table
    products = Product.objects.all()
    # let's save the data and make sure is available in the template
    # we are returning the template we want to use and the data we need
    return render(request, 'store/home.html', {'products': products})
