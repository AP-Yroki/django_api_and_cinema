from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category, Manufacturer
# from .models import Meal, Ingredients
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

class ProductGet(APIView):
    def get(self, request, pk=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response('Product not exist')

        serializer = ProductSerializer(data=request.data, instance=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})


    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response('Product not exist')

        serializer = ProductSerializer(data=request.data, instance=product, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response('Product not exist')

        product.delete()
        return Response('Product deleted')

class ProductGetList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductOne(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            meal = Product.objects.get(pk=pk)
        except:
            return Response('Product not exist')

        serializer = ProductSerializer(data=request.data, instance=meal)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})


    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            meal = Product.objects.get(pk=pk)
        except:
            return Response('Meal not exist')

        serializer = ProductSerializer(data=request.data, instance=meal, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            meal = Product.objects.get(pk=pk)
        except:
            return Response('Meal not exist')

        meal.delete()
        return Response('Meal deleted')


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Product
# from .serializers import ProductSerializer
# from django.http import Http404
#
# class ProductGet(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response({'data': serializer.data})
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
#
#     def retrieve(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404("Product not exist")
#
#         serializer = ProductSerializer(product)
#         return Response({'data': serializer.data})
#
#     def put(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404("Product not exist")
#
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'data': serializer.data})
#
#     def patch(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404("Product not exist")
#
#         serializer = ProductSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'data': serializer.data})
#
#     def delete(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404("Product not exist")
#
#         product.delete()
#         return Response('Product deleted')