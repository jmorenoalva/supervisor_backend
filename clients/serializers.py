from rest_framework import serializers
from utils.models import TypeDocument, Ubigeo
from employee.models import Promoter
from .models import TypeClient, Client, SitesClient, Contact
from .utils import validate_type_document, validate_type_client, validate_type_client_active

class TypeClientSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=4)
  description=serializers.CharField(max_length=255)
  status=serializers.BooleanField(default=True)

  class Meta:
    model=TypeClient
    fields=('__all__')

class ClientSerializer(serializers.ModelSerializer):
  code=serializers.CharField(max_length=20)
  type_client=serializers.PrimaryKeyRelatedField(queryset=TypeClient.objects.all())
  type_document=serializers.PrimaryKeyRelatedField(queryset=TypeDocument.objects.all())
  nro_document=serializers.CharField(max_length=20)
  company_name=serializers.CharField(max_length=255)
  fiscal_address=serializers.CharField(max_length=255)
  ubigeo=serializers.PrimaryKeyRelatedField(queryset=Ubigeo.objects.all())
  status=serializers.BooleanField(default=True)

  # def validate_type_client(self,value):
  #   return validate_type_client(value)
  # def validate_type_client_active(self,value):
  #   return validate_type_client_active(value)
  # def validate_type_document(self, value):
  #   return validate_type_document(value)

  # def error_messages(self):
  #   error_messages=super().error_messages
  #   error_messages.update({
  #     'validate_type_client':self.validate_type_client,
  #     # 'validate_type_client_active': self.validate_type_client_active,
  #   })
  #   return error_messages

  class Meta:
    model=Client
    fields=('__all__')

  # def to_representation(self, instance):
  #   data=super().to_representation(instance)
  #   data['type_client']=instance.type_client.id
  #   return super().to_representation(instance)

class SitesClientSerializer(serializers.ModelSerializer):
  client=serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
  code=serializers.CharField(max_length=4)
  comercial_name=serializers.CharField(max_length=255)
  address=serializers.CharField(max_length=255)
  ubigeo=serializers.PrimaryKeyRelatedField(queryset=Ubigeo.objects.all())
  promoter=serializers.PrimaryKeyRelatedField(queryset=Promoter.objects.all())
  status=serializers.BooleanField(default=True)

  class Meta:
    model=SitesClient
    fields=('__all__')

class ContactSerializer(serializers.ModelSerializer):
  sites_client=serializers.PrimaryKeyRelatedField(queryset=SitesClient.objects.all())
  item=serializers.IntegerField()
  name=serializers.CharField(max_length=255)
  phone=serializers.CharField(max_length=255)
  email=serializers.CharField(max_length=255)
  status=serializers.BooleanField(default=True)

  class Meta:
    model=Contact
    fields=('__all__')
