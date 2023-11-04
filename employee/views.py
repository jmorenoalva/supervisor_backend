from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Supervisor, Zone, Promoter, Quota, Level, Employee
from .serializers import SupervisorSerializer, ZoneSerializer, PromoterSerializer, QuotaSerializer, LevelSerializer, EmployeeSerializer

# Create your views here.
class SupervisorViews(GenericAPIView):
  serializer_class=SupervisorSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Supervisor.objects.all()

  def post(self, request):
    serializer=SupervisorSerializer(data=request.data)
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
      item=Supervisor.objects.get(id=id)
      serializer=SupervisorSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Supervisor.objects.all()
    serializer=SupervisorSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Supervisor, id=id)
    serializer=SupervisorSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Supervisor, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class ZoneViews(GenericAPIView):
  serializer_class=ZoneSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Zone.objects.all()

  def post(self, request):
    serializer=ZoneSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data":serializer.data
      },status=status.HTTP_200_OK)
    else:
      return Response({
        "status":"error",
        "data":serializer.data
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      item=Zone.objects.get(id=id)
      serializer=ZoneSerializer(item)
      return Response({
        "status": "success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Zone.objects.all()
    serializer=ZoneSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Zone, id=id)
    serializer=ZoneSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Zone, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class PromoterViews(GenericAPIView):
  serializer_class=PromoterSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Promoter.objects.all()

  def post(self, request):
    serializer=PromoterSerializer(data=request.data)
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
      item=Promoter.objects.get(id=id)
      serializer=PromoterSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Promoter.objects.all()
    serializer=PromoterSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Promoter, id=id)
    serializer=PromoterSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Promoter, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class QuotaViews(GenericAPIView):
  serializer_class=QuotaSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Quota.objects.all()

  def post(self, request):
    serializer=QuotaSerializer(data=request.data)
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
      item=Quota.objects.get(id=id)
      serializer=QuotaSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Quota.objects.all()
    serializer=QuotaSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Quota, id=id)
    serializer=QuotaSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Quota, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class LevelViews(GenericAPIView):
  serializer_class=LevelSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Level.objects.all()

  def post(self, request):
    serializer=LevelSerializer(data=request.data)
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
      item=Level.objects.get(id=id)
      serializer=LevelSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Level.objects.all()
    serializer=LevelSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Level, id=id)
    serializer=LevelSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Level, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class EmployeeViews(GenericAPIView):
  serializer_class=EmployeeSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Employee.objects.all()

  def post(self, request):
    serializer=EmployeeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({
        "status":"success",
        "data": serializer.data
      }, status=status.HTTP_200_OK)
    else:
      return Response({
        "status":"error",
        "data":serializer.data
      }, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request, id=None):
    if id:
      item=Employee.objects.get(id=id)
      serializer=EmployeeSerializer(item)
      return Response({
        "status":"success",
        "data":serializer.data
      }, status=status.HTTP_200_OK)

    items=Employee.objects.all()
    serializer=EmployeeSerializer(items,many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Employee, id=id)
    serializer=EmployeeSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Employee, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })