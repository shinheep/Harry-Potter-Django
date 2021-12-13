from rest_framework import serializers
from ..models.school import School
from .house import HouseSerializer

class SchoolSerializer(serializers.ModelSerializer):
    houses = HouseSerializer(many=True, read_only=True)
    class Meta:
        model = School
        fields = ('id', 'name', 'location', 'owner', 'houses')