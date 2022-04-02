import sys
from django.db import models


# Create your models here.
class Point(models.Model):
	title = models.CharField(max_length=255, unique=True)
	description = models.TextField()
	image = models.CharField(max_length=255, blank=True)
	code = models.CharField(max_length=255, blank=True)
	last_update = models.DateTimeField(auto_now=True)
	time_created = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		self.code = hash(self.title) % ((sys.maxsize + 1) * 2)
		super().save(*args, **kwargs)
		

	def __str__(self) -> str:
		return self.title