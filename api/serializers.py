from rest_framework import serializers

from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    sum = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    def get_sum(self, obj):
        return obj.price*obj.quantity


class ProductByFullSumSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    total_sum = serializers.FloatField()