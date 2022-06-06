from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('_id')
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRental(APIView):
    def post(self, request, format=None):
        data = request.data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.get(_id=data.get('_id'))
            # Calculate Rent & Send Response
            product.rented_at = data['rented_at']
            product.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
