from rest_framework import serializers
from .models import Juice

class JuiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Juice
    fields = [
      'id',
      'name',
      'price',
      'description'
    ]