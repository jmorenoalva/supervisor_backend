from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

from .models import TypeClient, Client, SitesClient, Contact
from .serializers import TypeClientSerializer, ClientSerializer, SitesClientSerializer, ContactSerializer


# Create your views here.
class TypeClientViews(GenericAPIView):
  serializer_class=TypeClientSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return TypeClient.objects.all()

  def post(self, request):
    serializer=TypeClientSerializer(data=request.data)
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
      item=TypeClient.objects.get(id=id)
      serializer=TypeClientSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=TypeClient.objects.all()
    serializer=TypeClientSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)

    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    #item=Type_client.objects.get(id=id)
    item=get_object_or_404(TypeClient, id=id)
    serializer=TypeClientSerializer(item,data=request.data, partial=True)
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
    item=get_object_or_404(TypeClient, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })
type_client_views = TypeClientViews()
class ClientViews(GenericAPIView):
  serializer_class=ClientSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Client.objects.all()

  def post(self, request):
    serializer=ClientSerializer(data=request.data)

    # serializer.validate_type_client()

    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "message":serializer.errors,
        "data":serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response({
        "status":"error",
        "message":serializer.errors,
        "data":serializer.data
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      item=Client.objects.get(id=id)
      serializer=ClientSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Client.objects.all()
    serializer=ClientSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data":self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Client, id=id)
    serializer=ClientSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Client, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class SitesClientViews(GenericAPIView):
  serializer_class=SitesClientSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return SitesClient.objects.all()

  def post(self, request):
    serializer=SitesClientSerializer(data=request.data)
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
      item=SitesClient.objects.get(id=id)
      serializer=SitesClientSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=SitesClient.objects.all()
    serializer=SitesClientSerializer(items,many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data":self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(SitesClient, id=id)
    serializer=SitesClientSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(SitesClient, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class ContactViews(GenericAPIView):
  serializer_class=ContactSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Contact.objects.all()

  def post(self, request):
    serializer=ContactSerializer(data=request.data)
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
      item=Contact.objects.get(id=id)
      serializer=ContactSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)
    items=Contact.objects.all()
    serializer=ContactSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data":self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Contact, id=id)
    serializer=ContactSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Contact, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })