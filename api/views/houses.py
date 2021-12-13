from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.school import HouseSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.house import House

class HousesView(APIView):
  def post(self, request):
    house = HouseSerializer(data=request.data)
    if house.is_valid():
      house.save()
      return Response(house.data, status=status.HTTP_201_CREATED)
    else:
      return Response(house.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def get(self, request):
    houses = House.objects.all()
    data = HouseSerializer(houses, many=True).data
    return Response(data)

class HouseView(APIView):
  def patch(self, request, id):
    house = get_object_or_404(House, id=id)
    updated_house = HouseSerializer(house, data=request.data, partial=True)
    if updated_house.is_valid():
      updated_house.save()
      return Response(updated_house.data)
  
  def put(self, request, id):
    house = get_object_or_404(House, id=id)
    updated_house = HouseSerializer(house, data=request.data)
    if updated_house.is_valid():
      updated_house.save()
      return Response(updated_house.data)
  
  def delete(self, request, id):
    house = get_object_or_404(House, id=id)
    house.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def get(self, request, id):
    house = get_object_or_404(House, id=id)
    data = HouseSerializer(house).data
    return Response(data)
