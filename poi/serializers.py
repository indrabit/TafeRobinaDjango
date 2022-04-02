from rest_framework import serializers
from poi.models import Point

class PointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Point
		fields = ['title', 'description', 'image']