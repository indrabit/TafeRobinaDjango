from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from campus import serializers

# Create your views here.
@api_view(['GET'])
def campus_list(request):
	queryset = Campus.objects.all()
	serializer = CampusSerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def regions_list(request):
	queryset = Region.objects.all()
	serializer = RegionSerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def menu_category_list(request):
	queryset = MenuCategory.objects.all()
	serializer = MenuCategorySerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def menu_items_list(request):
	queryset = MenuItem.objects.all()
	serializer = MenuItemSerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def events_list(request):
	queryset = Event.objects.all()
	serializer = EventSerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def events_upcoming(request):
	queryset = Event.objects.filter(
		listed=True
	).filter(
		event_start__gte=datetime.today()
	)
	serializer = EventSerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def users_list(request):
	queryset = User.objects.all()
	serializer = UserSerializer(queryset, many=True)
	return Response(serializer.data)