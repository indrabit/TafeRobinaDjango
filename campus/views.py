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
	try:
		campuses = Campus.objects.filter(
			listed=True
		)
		serializer = CampusSerializer(campuses, many=True)
		return Response(serializer.data)
	except Campus.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def campus_detail(request, id):
	try:
		campus = Campus.objects.get(id=id)
		serializer = CampusSerializer(campus)
		return Response(serializer.data)
	except Campus.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def regions_list(request):
	try:
		regions = Region.objects.filter(
			listed=True
		)
		serializer = RegionSerializer(regions, many=True)
		return Response(serializer.data)
	except Region.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def regions_campuses(request, id):
	try:
		campusRegions = Campus.objects.filter(
			region=id
		).filter(
			listed=True
		)
		serializer = CampusSerializer(campusRegions, many=True)
		return Response(serializer.data)
	except Campus.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def menu_category_list(request):
	queryset = MenuCategory.objects.all()
	serializer = MenuCategorySerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def menu_category_campus(request, campus):
	try:
		menuCategories = MenuCategory.objects.filter(
			campus=campus
		).filter(
			listed=True
		)
		serializer = MenuCategorySerializer(menuCategories, many=True)
		return Response(serializer.data)
	except MenuCategory.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def menu_items_list(request):
	queryset = MenuItem.objects.all()
	serializer = MenuItemSerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def menu_items_category(request, category):
	try:
		menuItems = MenuItem.objects.filter(
			category=category
		).filter(
			listed=True
		)
		serializer = MenuItemSerializer(menuItems, many=True)
		return Response(serializer.data)
	except MenuItem.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)


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