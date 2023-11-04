from rest_framework import serializers
from .models import TypeDocument, Ubigeo, TypeInvoice, Period

class TypeDocumentSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=2)
  alias=serializers.CharField(max_length=10)
  description=serializers.CharField(max_length=254, required=False)
  status=serializers.BooleanField(default=True)

  def validate_code(self, value):
    if TypeDocument.objects.filter(code=value).exists():
      raise serializers.ValidationError('El código ya existe.')
    return value

  class Meta:
    model=TypeDocument
    fields=('__all__')

class UbigeoSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=6)
  region=serializers.CharField(max_length=100)
  city=serializers.CharField(max_length=100)
  district=serializers.CharField(max_length=100)
  status=serializers.BooleanField(default=True)

  def validate_code(self, value):
    if Ubigeo.objects.filter(code=value).exists():
      raise serializers.ValidationError('El código ya existe.')
    return value

  class Meta:
    model=Ubigeo
    fields=('__all__')

class TypeInvoiceSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=2)
  description=serializers.CharField(max_length=100)
  status=serializers.BooleanField(default=True)

  def validate_code(self, value):
    if TypeInvoice.objects.filter(code=value).exists():
      raise serializers.ValidationError('El código ya existe.')
    return value

  class Meta:
    model=TypeInvoice
    fields=('__all__')

class PeriodSerializer(serializers.ModelSerializer):
  period=serializers.CharField(max_length=7)
  year=serializers.IntegerField()
  month=serializers.CharField(max_length=2)
  status=serializers.BooleanField(default=True)

  def validate_period(self, value):
    if Period.objects.filter(period=value).exists():
      raise serializers.ValidationError('El periodo ya existe.')
    return value

  class Meta:
    model=Period
    fields=('__all__')