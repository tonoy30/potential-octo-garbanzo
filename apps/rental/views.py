from dateutil import parser
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all().order_by('_id')
        availability = self.request.query_params.get('availability')
        if availability is not None:
            queryset = queryset.filter(availability=availability)
        return queryset


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRental(ViewSet):
    def calculate_product_rent(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.get(_id=request.data.get('_id'))
            # Calculate Rent & Send Response
            rented_at = parser.parse(request.data['rented_at'])
            returned_at = parser.parse(request.data['returned_at'])

            total_rental_period_days = (returned_at - rented_at).days
            minimum_rental_period = product.minimum_rent_period

            if (product.type == 'meter' and total_rental_period_days * 10 > product.mileage):
                return Response({'error': 'This product is not available for your asking requirement'},
                                status=status.HTTP_400_BAD_REQUEST)

            if (total_rental_period_days < minimum_rental_period):
                return Response({'error': 'Minimum rent period is not satisfied'},
                                status=status.HTTP_400_BAD_REQUEST)

            total_rent = float(product.price) * total_rental_period_days
            if (total_rental_period_days > minimum_rental_period and product.discount > 0):
                discount = (total_rent * product.discount) / 100
                total_rent = total_rent - discount

            product.rented_at = rented_at
            product.returned_at = returned_at
            product.save()

            return Response({'id': product._id, 'discount': product.discount, 'total_rent': total_rent,
                            'rented_at': rented_at, 'returned_at': returned_at},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def confirmed_product_rent(self, request):
        product = Product.objects.get(_id=request.data.get('id'))
        if product is not None:
            product.availability = False
            product.save()
            return Response({'id': product._id, 'message': f'{product.name} rented successfully'},
                            status=status.HTTP_201_CREATED)
        return Response({'error': 'product not found'}, status=status.HTTP_400_BAD_REQUEST)

    # NOTE: For simplicity I can assume all user will return the rented product on time
    def return_product(self, request):
        product = Product.objects.get(_id=request.data.get('id'))
        if product is not None:
            product.availability = True
            # Calculate durability
            rented_at = product.rented_at
            returned_at = product.returned_at
            total_rental_period_days = (returned_at - rented_at).days
            durability = product.durability

            if (product.type == 'meter'):
                total_durability = durability - \
                    total_rental_period_days * 2 - \
                    (total_rental_period_days * 10) * 2
                product.durability = total_durability if total_durability > 0 else 0
            else:
                product.durability = durability - total_rental_period_days

            product.needing_repair = product.durability <= 0
            product.rented_at = None
            product.returned_at = None
            product.save()
            return Response({'message': f'{product.name} returned successfully'},
                            status=status.HTTP_201_CREATED)
        return Response({'error': 'product not found'}, status=status.HTTP_400_BAD_REQUEST)
