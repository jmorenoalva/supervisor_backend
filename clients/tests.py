from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Client
from .serializers import ClientSerializer

# Create your tests here.
class ClientSerializerTests(TestCase):

  def test_validate_type_client_not_found(self):
    data={
      'code':'12',
      'type_client':1
    }

    serializer = ClientSerializer(data=data)

    with self.assertRaises(ValidationError):
      serializer.validate(data)

  def test_validate_type_client_exists(self):
    data = {
      'code': '12',
      'type_client': 1,
    }

    serializer = ClientSerializer(data=data)

    serializer.is_valid()

    self.assertEqual(serializer.validated_data, data)