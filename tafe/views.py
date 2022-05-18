from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from tafe import serializers

# Returns a list of all Regions.
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

# Returns a list of all Campuses.
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

# Returns Information about a Campus.
@api_view(['GET'])
def campus_detail(request, id):
	try:
		campus = Campus.objects.get(id=id)
		serializer = CampusSerializer(campus)
		return Response(serializer.data)
	except Campus.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

# Returns the Trading Hours of a Campus
@api_view(['GET'])
def campus_hours(request, campusID):
    try:
        campusHours = CampusHours.objects.get(campus=campusID)
        serializer = CampusHoursSerializer(campusHours)
        return Response(serializer.data)
    except CampusHours.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

# Returns a list of all Campuses from a Region.
@api_view(['GET'])
def region_campuses(request, regionID):
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

# Returns a list of Resturants for a given Campus.
@api_view(['GET'])
def resturant_list(request, campusID):
	try:
		resturants = Restaurant.objects.filter(
			campus=campusID
		).filter(
			listed=True
		)
		serializer = RestaurantSerializer(resturants, many=True)
		return Response(serializer.data)
	except Restaurant.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

# Returns the Trading Hours of a Resturant
@api_view(['GET'])
def resturant_hours(request, resturantID):
    try:
        resturantHours = RestaurantHours.objects.get(campus=resturantID)
        serializer = RestaurantHoursSerializer(resturantHours)
        return Response(serializer.data)
    except RestaurantHours.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

# Returns a list of ALL Events.
@api_view(['GET'])
def events_list(request):
	queryset = Event.objects.all()
	serializer = EventSerializer(queryset, many=True)
	return Response(serializer.data)

# Returns a list of Upcoming Events.
@api_view(['GET'])
def events_upcoming(request):
	queryset = Event.objects.filter(
		listed=True
	).filter(
		eventStart__gte=datetime.today()
	)
	serializer = EventSerializer(queryset, many=True)
	return Response(serializer.data)