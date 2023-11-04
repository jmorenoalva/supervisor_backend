from rest_framework import serializers
from .models import UserManager,User

class registerUserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=["username","email", "names", "last_names", "password"]