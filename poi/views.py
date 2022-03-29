from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Point
from .serializers import PointSerializer
from poi import serializers

# Create your views here.
@api_view(['GET'])
def points_list(request):
	queryset = Point.objects.all()
	serializer = PointSerializer(queryset, many=True)
	return Response(serializer.data)
	
@api_view(['GET'])
def point_detail(request, id):
	try:
		point = Point.objects.get(pk=id)
		serializer = PointSerializer(point)
		return Response(serializer.data)
	except Point.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)