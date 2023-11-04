from rest_framework import serializers
from .models import TypeClient, Client
from utils.models import TypeDocument, Ubigeo

def validate_type_client(value):
  if not TypeClient.objects.filter(id=value).exists():
    return serializers.ValidationError('El tipo de cliente no existe.')
  return value

def validate_type_client_active(value):
  if not TypeClient.objects.filter(id=value, status=True).exists():
    raise serializers.ValidationError('El tipo de cliente esta inactivo.')
  return value

def validate_type_document(value):
  try:
    TypeDocument.objects.get(id=value)
  except TypeDocument.DoesNotExist:
    raise serializers.ValidationError('El tipo de documento no existe.')
  return value

def validate_type_ubigeo(value):
  try:
    Ubigeo.objects.get(id=value)
  except Ubigeo.DoesNotExist:
    raise serializers.ValidationError('El Ubigeo no existe.')
  return value

def validate_code(value):
  if Client.objects.filter(code=value).exists():
    raise serializers.ValidationError('El codigo ya existe.')
  return value
#validacion
def validate_document(value):
  if Client.objects.filter(nro_document=value).exists():
    raise serializers.ValidationError('El numero de documento ya existe.')
  return value