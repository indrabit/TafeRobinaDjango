from django.db import models

# Create your models here.
class Point(models.Model):
	title = models.CharField(max_length=255)
	discription = models.TextField()
	image = models.CharField(max_length=255)
	last_update = models.DateTimeField(auto_now=True)
	time_created = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.title