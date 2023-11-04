from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination

from .models import TypeDocument, Ubigeo, TypeInvoice, Period
from .serializers import TypeDocumentSerializer, UbigeoSerializer, TypeInvoiceSerializer, PeriodSerializer

# Create your views here.
class TypeDocumentViews(GenericAPIView):
  serializer_class=TypeDocumentSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return TypeDocument.objects.all()

  def post(Self, request):
    serializer=TypeDocumentSerializer(data=request.data)
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
    queryset=TypeDocument.objects.all()

    if id:
      item=TypeDocument.objects.get(id=id)
      serializer=TypeDocumentSerializer(item)
      return Response({
        "status":"success",
        "data": serializer.data
      }, status=status.HTTP_200_OK)

    if request.GET.get('alias'):
      alias=request.GET.get('alias')
      queryset=queryset.filter(alias__icontains=alias)
      return Response({
        "status":"success",
        "data":[alias.to_dict() for alias in queryset]
      })

    if request.GET.get('description'):
      description=request.GET.get('description')
      queryset=queryset.filter(description__icontains=description)
      return Response({
        "status":"success",
        "data":[description.to_dict() for description in queryset]
      })

    items=TypeDocument.objects.all()
    serializer=TypeDocumentSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(TypeDocument, id=id)
    serializer=TypeDocumentSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(TypeDocument, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class UbigeoViews(GenericAPIView):
  serializer_class=UbigeoSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Ubigeo.objects.all()

  def post(self, request):
    serializer=UbigeoSerializer(data=request.data)
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
    queryset=Ubigeo.objects.all()

    if id:
      item=Ubigeo.objects.get(id=id)
      serializer=UbigeoSerializer(item)
      return Response({
        "status":"success",
        "data": serializer.data
      }, status=status.HTTP_200_OK)

    if request.GET.get('code'):
      code=request.GET.get('code')
      queryset=queryset.filter(code__exact=code)
      return Response({
        "status":"success",
        "data":[code.to_dict() for code in queryset]
      })

    if request.GET.get('district'):
      district=request.GET.get('district')
      queryset=queryset.filter(district__contains=district)
      return Response({
        "status":"success",
        "data":[district.to_dict() for district in queryset]
      })

    items=Ubigeo.objects.all()
    serializer=UbigeoSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Ubigeo, id=id)
    serializer=UbigeoSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Ubigeo, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class TypeInvoiceViews(GenericAPIView):
  serializer_class=TypeInvoiceSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return TypeInvoice.objects.all()

  def post(self, request):
    serializer=TypeInvoiceSerializer(data=request.data)
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
    queryset=TypeInvoice.objects.all()

    if id:
      item=TypeInvoice.objects.get(id=id)
      serializer=TypeInvoiceSerializer(item)
      return Response({
        "status":"success",
        "data": serializer.data
      }, status=status.HTTP_200_OK)

    if request.GET.get('code'):
      code=request.GET.get('code')
      queryset=queryset.filter(code__exact=code)
      return Response({
        "status":"success",
        "data":[code.to_dict() for code in queryset]
      })

    if request.GET.get('description'):
      description=request.GET.get('description')
      queryset=queryset.filter(description__contains=description)
      return Response({
        "status":"success",
        "data":[description.to_dict() for description in queryset]
      })

    items=TypeInvoice.objects.all()
    serializer=TypeInvoiceSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(TypeInvoice, id=id)
    serializer=TypeInvoiceSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(TypeInvoice, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })

class PeriodViews(GenericAPIView):
  serializer_class=PeriodSerializer
  pagination_class=PageNumberPagination

  def get_queryset(self):
    return Period.objects.all()

  filterset_fields=['id','period']

  def post(self, request):
    serializer=PeriodSerializer(data=request.data)
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
    queryset=Period.objects.all()
    if id:
      item=Period.objects.get(id=id)
      serializer=PeriodSerializer(item)
      return Response({
        "status":"success",
        "data": serializer.data
      }, status=status.HTTP_200_OK)

    if request.GET.get('period'):
      period=request.GET.get('period')
      queryset=queryset.filter(period__exact=period)
      return Response({
        "status":"success",
        "data":[period.to_dict() for period in queryset]
      },status=status.HTTP_200_OK)
    if request.GET.get('year'):
      year=request.GET.get('year')
      #queryset=queryset.filter(year__contains=year)
      queryset=queryset.filter(year__exact=year)
      return Response({
        "status":"success",
        "data":[year.to_dict() for year in queryset]
      },status=status.HTTP_200_OK)
    if request.GET.get('month'):
      month=request.GET.get('month')
      queryset=queryset.filter(month__exact=month)
      return Response({
        "status":"success",
        "data":[month.to_dict() for month in queryset]
      },status=status.HTTP_200_OK)

    items=Period.objects.all()
    serializer=PeriodSerializer(items, many=True)
    # return Response({
    #   "status":"success",
    #   "data":serializer.data
    # }, status=status.HTTP_200_OK)
    return self.get_paginated_response({
      "status":"success",
      "data": self.paginate_queryset(serializer.data)
    })

  def patch(self, request, id=None):
    item=get_object_or_404(Period, id=id)
    serializer=PeriodSerializer(item, data=request.data, partial=True)
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
    item=get_object_or_404(Period, id=id)
    item.delete()
    return Response({
      "status":"success",
      "data":"Item Deleted"
    })