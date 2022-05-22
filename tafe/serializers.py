from rest_framework import serializers
from tafe.models import *

class RegionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Region
		fields = [
			'id',
			'name',
		]



class CampusHoursSerializer(serializers.ModelSerializer):
	class Meta:
		model = CampusHours
		fields = [
			'campus',
			'monOpen',
			'monClose',
			'tueOpen',
            'tueClose',
            'wedOpen',
            'wedClose',
            'thurOpen',
            'thurClose',
            'friOpen',
            'friClose',
            'satOpen',
            'satClose',
            'sunOpen',
            'sunClose',
		]

class CampusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Campus
		fields = [
			'id',
			'region',
			'name',
			'description',
			'address',
			'latitude',
			'longitude',
		]

class RestaurantSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields = [
			'id',
			'campus',
			'name',
			'description',
			'address',
            'image',
            'menuLink',
            'bookingLink',
		]

class RestaurantHoursSerializer(serializers.ModelSerializer):
	class Meta:
		model = RestaurantHours
		fields = [
			'resgion',
			'monOpen',
			'monClose',
			'tueOpen',
            'tueClose',
            'wedOpen',
            'wedClose',
            'thurOpen',
            'thurClose',
            'friOpen',
            'friClose',
            'satOpen',
            'satClose',
            'sunOpen',
            'sunClose',
		]

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = [
			'id',
			'title',
			'description',
			'content',
			'location',
            'registerLink',
            'image',
            'eventStart',
            'eventEnd',
		]

class IndustrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Industry
		fields = [
			'id',
			'name',
		]

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
			'id',
			'industry',
			'region',
			'campus',
			'notificationToken',
		]