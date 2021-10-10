from django.db.models import fields
from .models import item,user
from rest_framework import serializers

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'

        