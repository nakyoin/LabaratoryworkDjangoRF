from django.shortcuts import render
from djoser.conf import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.forms.models import model_to_dict
from rest_framework import generics, permissions, status, viewsets

from .permissions import IsAdminOrReadOnly
from .serializers import *
from rest_framework.generics import *


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def order_all(request):
    if request.method == 'GET':
        orderss = Order.objects.all()
        serializers = OrderSerializer(orderss, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = OrderSerializer
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def product_all(request):
     if request.method == 'GET':
         products = Product.objects.all()
         serializers = ProductSerializer(products, many=True)
         return Response(serializers.data, status=status.HTTP_200_OK)
     elif request.method == 'POST':
         serializer = ProductSerializer
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def product_detail(request, pk):
     try:
         product = Product.objects.get(pk=pk)
     except:
         return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method == 'GET':
         serializer = ProductSerializer(product)
         return Response(serializer.data, status=status.HTTP_200_OK)
     elif request.method == 'PUT':
         serializer = ProductSerializer(Product, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(status=status.HTTP_201_CREATED)
         return Response(status=status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
         product.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def worker_all(request):
     if request.method == 'GET':
         workers = Workers.objects.all()
         serializers = WorkersSerializer(workers, many=True)
         return Response(serializers.data, status=status.HTTP_200_OK)
     elif request.method == 'POST':
         serializer = WorkersSerializer
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def worker_detail(request, pk):
     try:
         workers = Workers.objects.get(pk=pk)
     except:
         return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method == 'GET':
         serializer = WorkersSerializer(workers)
         return Response(serializer.data, status=status.HTTP_200_OK)
     elif request.method == 'PUT':
         serializer = WorkersSerializer(Workers, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(status=status.HTTP_201_CREATED)
         return Response(status=status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
         workers.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def change_all(request):
     if request.method == 'GET':
         changes = Change.objects.all()
         serializers = ChangeSerializer(changes, many=True)
         return Response(serializers.data, status=status.HTTP_200_OK)
     elif request.method == 'POST':
         serializer = ChangeSerializer
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def change_detail(request, pk):
     try:
         changes = Change.objects.get(pk=pk)
     except:
         return Response(status=status.HTTP_404_NOT_FOUND)
     if request.method == 'GET':
         serializer = ChangeSerializer(changes)
         return Response(serializer.data, status=status.HTTP_200_OK)
     elif request.method == 'PUT':
         serializer = ChangeSerializer(Change, data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(status=status.HTTP_201_CREATED)
         return Response(status=status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
         changes.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)








