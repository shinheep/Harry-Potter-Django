from rest_framework import serializers
from ..models.house import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'