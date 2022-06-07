from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductDetail, ProductList, ProductRental

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='products-details'),
    path('products/rent',
         ProductRental.as_view({'post': 'calculate_product_rent'}), name='products-rent'),
    path('products/rent/confirmed', ProductRental.as_view({'post': 'confirmed_product_rent'}),
         name='products-rent-confirmed'),
    path('products/return', ProductRental.as_view({'post': 'return_product'}),
         name='products-rent-return'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
