from django.urls import path

from . import views

# let's match the name with the core>urls.py file
app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
]