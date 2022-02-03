from django.urls import path

from . import views

# let's match the name with the core>urls.py file
app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
