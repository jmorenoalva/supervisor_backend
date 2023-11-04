from rest_framework import serializers
from users.models import User
from utils.models import TypeDocument, Ubigeo
from .models import Supervisor, Zone, Promoter, Quota, Level, Employee

class SupervisorSerializer(serializers.ModelSerializer):
  user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  code=serializers.CharField(max_length=10)
  table=serializers.CharField(max_length=10)
  status=serializers.BooleanField(default=True)

  class Meta:
    model=Supervisor
    fields=('__all__')

class ZoneSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=10)
  description=serializers.CharField(max_length=255)
  supervisor=serializers.PrimaryKeyRelatedField(queryset=Supervisor.objects.all())
  status=serializers.BooleanField(default=True)

  class Meta:
    model=Zone
    fields=('__all__')

class PromoterSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=10)
  user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  zone=serializers.PrimaryKeyRelatedField(queryset=Zone.objects.all())
  status=serializers.BooleanField(default=True)

  class Meta:
    model=Promoter
    fields=('__all__')

class QuotaSerializer(serializers.ModelSerializer):
  anio=serializers.IntegerField()
  mes=serializers.CharField(max_length=2)
  periodo=serializers.CharField(max_length=7)
  quota=serializers.DecimalField(max_digits=13, decimal_places=3)
  zone=serializers.PrimaryKeyRelatedField(queryset=Zone.objects.all())
  status=serializers.BooleanField(default=True)

  class Meta:
    model=Quota
    fields=('__all__')

class LevelSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=10)
  description=serializers.CharField(max_length=255)
  status=serializers.BooleanField(default=True)

  class Meta:
    model=Level
    fields=('__all__')

class EmployeeSerializer(serializers.ModelSerializer):
  user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  type_document=serializers.PrimaryKeyRelatedField(queryset=TypeDocument.objects.all())
  number_document=serializers.CharField(max_length=254)
  phone=serializers.CharField(max_length=254)
  avatar=serializers.ImageField(max_length=200, required=False)
  address=serializers.CharField(max_length=254)
  ubigeo=serializers.PrimaryKeyRelatedField(queryset=Ubigeo.objects.all())
  level=serializers.PrimaryKeyRelatedField(queryset=Level.objects.all())

  class Meta:
    model=Employee
    fields=('__all__')