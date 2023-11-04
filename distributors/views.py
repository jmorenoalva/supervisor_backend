from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Distributor, ProductDistributor, Sales
from .serializers import DistributorSerializer, ProductDistributorSerializer, SalesSerializer

# Create your views here.
class DistributorViews(GenericAPIView):
  serializer_class=DistributorSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Distributor.objects.all()

  def post(self, request):
    serializer=DistributorSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response({
        "status":"error",
        "data":serializer.data
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      item=Distributor.objects.get(id=id)
      serializer=DistributorSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    item=Distributor.objects.all()
    serializer=DistributorSerializer(item, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data":self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Distributor, id=id)
    serializer=DistributorSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data":serializer.data
      })
    else:
      return Response({
        "status":"error",
        "data":serializer.errors
      })

  def delete(self, request, id=None):
    item=get_object_or_404(Distributor, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class ProductDistributorViews(GenericAPIView):
  serializer_class=ProductDistributorSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return ProductDistributor.objects.all()

  def post(self, request):
    serializer=ProductDistributorSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response({
        "status":"error",
        "data":serializer.data
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      item=ProductDistributor.objects.get(id=id)
      serializer=ProductDistributorSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=ProductDistributor.objects.all()
    serializer=ProductDistributorSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(ProductDistributor, id=id)
    serializer=ProductDistributorSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data":serializer.data
      })
    else:
      return Response({
        "status":"error",
        "data":serializer.errors
      })

  def delete(self, request, id=None):
    item=get_object_or_404(ProductDistributor, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class SalesViews(GenericAPIView):
  serializer_class=SalesSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Sales.objects.all()

  def post(self, request):
    serializer=SalesSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response({
        "status":"error",
        "data":serializer.data
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      item=Sales.objects.get(id=id)
      serializer=SalesSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Sales.objects.all()
    serializer=SalesSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data": serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data":self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Sales, id=id)
    serializer=SalesSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data":serializer.data
      })
    else:
      return Response({
        "status":"error",
        "data":serializer.errors
      })

  def delete(self, request, id=None):
    item=get_object_or_404(Sales, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })