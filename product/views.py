from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Unit, ActiveIngredient, Presentation, Product
from .serializers import UnitSerializer, ActiveIngredientSerializer, PresentationSerializer, ProductSerializer

# Create your views here.
class UnitViews(GenericAPIView):
  serializer_class=UnitSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Unit.objects.all()

  def post(self, request):
    serializer=UnitSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"succes",
        "data":serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response({
        "status":"error",
        "data":serializer.data
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      item=Unit.objects.get(id=id)
      serializer=UnitSerializer(item)
      return Response({
        "status":"success",
        "data": serializer.data
      }, status=status.HTTP_200_OK)

    items=Unit.objects.all()
    serializer=UnitSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Unit, id=id)
    serializer=UnitSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Unit, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class ActiveIngredientViews(GenericAPIView):
  serializer_class=ActiveIngredientSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return ActiveIngredient.objects.all()

  def post(self, request):
    serializer=ActiveIngredient(data=request.data)
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
      item=ActiveIngredient.objects.get(id=id)
      serializer=ActiveIngredient(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=ActiveIngredient.objects.all()
    serializer=ActiveIngredientSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(ActiveIngredient, id=id)
    serializer=ActiveIngredientSerializer(item, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data": serializer.data
      })
    else:
      return Response({
        "status":"error",
        "data":serializer.errors
      })

  def delete(self, request, id=None):
    item=get_object_or_404(ActiveIngredient, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class PresentationViews(GenericAPIView):
  serializer_class=PresentationSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Presentation.objects.all()

  def post(self, request):
    serializer=PresentationSerializer(data=request.data)
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
      item=ActiveIngredient.objects.get(id=id)
      serializer=ActiveIngredientSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=ActiveIngredient.objects.all()
    serializer=ActiveIngredientSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(ActiveIngredient, id=id)
    serializer=ActiveIngredientSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(ActiveIngredient, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class ProductViews(GenericAPIView):
  serializer_class=ProductSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Product.objects.all()

  def post(self, request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status": "success",
        "data": serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response({
        "status":"error",
        "data": serializer.data
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      item=Product.objects.get(id=id)
      serializer=ProductSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Product.objects.all()
    serializer=ProductSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Product, id=id)
    serializer=ProductSerializer(item,data=request.data, partial=True)
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
    item=get_object_or_404(Product, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })