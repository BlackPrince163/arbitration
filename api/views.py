from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product
from api.serializers import ProductByFullSumSerializer

from api.services.full_sum_products import full_sum


class ProductListView(APIView):
    def get(self, request):
        total_sum = full_sum()
        serializer_class = ProductByFullSumSerializer(total_sum)
        return Response({"recommendation": serializer_class.data})
