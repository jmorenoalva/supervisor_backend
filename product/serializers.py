from rest_framework import serializers
from distributors.serializers import ProductDistributorSerializer
from distributors.models import ProductDistributor
from .models import Unit, ActiveIngredient, Presentation, Product

class UnitSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=10)
  description=serializers.CharField(max_length=255)
  status=serializers.BooleanField(default=True)

  def validate_code(self, value):
    if Unit.objects.filter(code=value).exists():
      raise serializers.ValidationError('El código ya existe.')
    return value

  class Meta:
    model=Unit
    fields=('__all__')

class ActiveIngredientSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=10)
  description=serializers.CharField(max_length=255)
  status=serializers.BooleanField(default=True)

  def validate_code(self, value):
    if ActiveIngredient.objects.filter(code=value).exists():
      raise serializers.ValidationError('El código ya existe.')
    return value

  class Meta:
    model=ActiveIngredient
    fields=('__all__')

class PresentationSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=10)
  description=serializers.CharField(max_length=255)
  status=serializers.BooleanField(default=True)

  def validate_code(self, value):
    if Presentation.objects.filter(code=value).exists():
      raise serializers.ValidationError('El código ya existe.')
    return value

  class Meta:
    model=Presentation
    fields=('__all__')

class ProductSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=10)
  description=serializers.CharField(max_length=255)
  unit=serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
  presentation=serializers.PrimaryKeyRelatedField(queryset=Presentation.objects.all())
  resolution=serializers.CharField(max_length=255)
  indication=serializers.CharField(max_length=255)
  #active_ingredient=serializers.ManyToManyField(Active_ingredient)
  active_ingredient=ActiveIngredientSerializer(many=True)
  product_distributor_codes=serializers.SerializerMethodField()
  status=serializers.BooleanField(default=True)

  def validate_code(self, value):
    if Product.objects.filter(code=value).exists():
      raise serializers.ValidationError('El código ya existe.')
    return value

  def get_product_distributor_codes(self, obj):
    return ProductDistributorSerializer(ProductDistributor.objects.filter(product=obj), many=True).data

  class Meta:
    model=Product
    fields=('__all__')
