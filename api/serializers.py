from rest_framework import serializers
from .models import Product



# title = serializers.CharField(max_length=100)
# description = serializers.CharField(max_length=300)
# price = serializers.IntegerField()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.save()
        return instance



