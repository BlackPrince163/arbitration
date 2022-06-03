from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from api.models import Product
from api.serializers import ProductByFullSumSerializer, ProductSerializer

from api.services.full_sum_products import full_sum


class ProductListView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def list(self, request, *args, **kwargs):
        total_sum = full_sum()
        serializer_class = ProductByFullSumSerializer(total_sum)
        return Response(serializer_class.data)
