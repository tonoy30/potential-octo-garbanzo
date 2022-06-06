from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductDetail, ProductList, ProductRental

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='products-details'),
    path('products/rent', ProductRental.as_view(), name='products-rent'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
