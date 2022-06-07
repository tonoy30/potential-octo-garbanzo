from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductDetail, ProductList, ProductRental

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<int:pk>', ProductDetail.as_view(), name='products-details'),
    path('rent',
         ProductRental.as_view({'post': 'calculate_product_rent'}), name='products-rent'),
    path('rent/confirmed', ProductRental.as_view({'post': 'confirmed_product_rent'}),
         name='products-rent-confirmed'),
    path('return', ProductRental.as_view({'post': 'return_product'}),
         name='products-rent-return'),
    path('return/confirmed', ProductRental.as_view({'post': 'confirmed_product_return'}),
         name='products-return-confirmed'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
