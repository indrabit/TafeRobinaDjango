from rest_framework import serializers
from campus.models import *

class RegionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Region
		fields = [
			'name',
			'description',
			'image',
		]

class CampusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Campus
		fields = [
			'region',
			'name',
			'description',
			'address',
			'image',
			'map',
		]

class MenuCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuCategory
		fields = [
			'campus'
			'name',
			'description',
			'image',
		]

class MenuItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = MenuItem
		fields = [
			'category',
			'name',
			'description',
			'price',
		]

class EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = [
			'location',
			'title',
			'description',
			'image',
			'event_start',
			'event_end',
		]
	location = serializers.StringRelatedField()

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = [
			'type',
			'campus',
			'name',
			'number',
		]