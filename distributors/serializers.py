from rest_framework import serializers
from utils.models import TypeDocument, Ubigeo
from product.models import Product
from clients.models import Client, SitesClient
from utils.models import Ubigeo, TypeInvoice, Period
from employee.models import Promoter
from .models import Distributor, ProductDistributor, Sales

class DistributorSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=4)
  type_document=serializers.PrimaryKeyRelatedField(queryset=TypeDocument.objects.all())
  nro_document=serializers.CharField(max_length=20)
  company_name=serializers.CharField(max_length=255)
  fiscal_address=serializers.CharField(max_length=255)
  ubigeo=serializers.PrimaryKeyRelatedField(queryset=Ubigeo.objects.all())
  status=serializers.BooleanField(default=True)

  class Meta:
    model=Distributor
    fields=('__all__')

class ProductDistributorSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=15)
  description=serializers.CharField(max_length=255)
  distributor=serializers.PrimaryKeyRelatedField(queryset=Distributor.objects.all())
  product=serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

  class Meta:
    model=ProductDistributor
    fields=('__all__')

class SalesSerializer(serializers.ModelSerializer):
  distributor=serializers.PrimaryKeyRelatedField(queryset=Distributor.objects.all())
  date=serializers.DateField()
  client=serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
  code_client=serializers.CharField(max_length=20)
  company_name=serializers.CharField(max_length=255)
  commercial_name=serializers.CharField(max_length=255)
  district=serializers.CharField(max_length=50)
  sites_client=serializers.PrimaryKeyRelatedField(queryset=SitesClient.objects.all())
  ubigeo=serializers.PrimaryKeyRelatedField(queryset=Ubigeo.objects.all())
  product=serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
  code_product=serializers.CharField(max_length=10)
  code_product_distributor_first=serializers.CharField( max_length=20)
  code_product_distributor_second=serializers.CharField( max_length=20)
  description_product=serializers.CharField(max_length=255)
  amount=serializers.IntegerField()
  value=serializers.DecimalField(max_digits=14, decimal_places=4)
  price=serializers.DecimalField(max_digits=14, decimal_places=4)
  promoter=serializers.PrimaryKeyRelatedField(queryset=Promoter.objects.all())
  code_promoter=serializers.CharField(max_length=10)
  name_promoter=serializers.CharField(max_length=255)
  code_vendedor=serializers.CharField(max_length=10)
  type_invoice=serializers.PrimaryKeyRelatedField(queryset=TypeInvoice.objects.all())
  serie_invoice=serializers.CharField(max_length=4)
  nro_invoice=serializers.CharField(max_length=8)
  period=serializers.PrimaryKeyRelatedField(queryset=Period.objects.all())

  class Meta:
    model=Sales
    fields=('__all__')