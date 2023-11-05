from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.core.exceptions import ValidationError
from .models import Client, TypeClient
from .serializers import ClientSerializer, TypeClientSerializer

# Create your tests here.
# class ClientSerializerTests(TestCase):

#   def test_validate_type_client_not_found(self):
#     data={
#       'code':'12',
#       'type_client':1
#     }

#     serializer = ClientSerializer(data=data)

#     with self.assertRaises(ValidationError):
#       serializer.validate(data)

#   def test_validate_type_client_exists(self):
#     data = {
#       'code': '12',
#       'type_client': 1,
#     }

#     serializer = ClientSerializer(data=data)

#     serializer.is_valid()

#     self.assertEqual(serializer.validated_data, data)

class TypeClientViewsTest(TestCase):
  def setUp(self):
      self.client = APIClient()
      self.type_client_data = {
          "code": "01",
          "description": "Tipo de Cliente B",
          "status": True
      }
      self.type_client = TypeClient.objects.create(**self.type_client_data)

  def test_get_type_client(self):
      url = reverse("type_client_views")
      response = self.client.get(url)
      self.assertEqual(response.status_code, 200)

  def test_create_type_client(self):
      new_type_client_data = {
          "code": "02",
          "description": "Nuevo Tipo de Cliente C",
          "status": True
      }
      url = reverse("type_client_views")
      response = self.client.post(url, new_type_client_data, format="json")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(TypeClient.objects.count(), 2)