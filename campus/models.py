from django.db import models

# Create your models here.
class Region(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(blank=True)
	image = models.CharField(max_length=255, blank=True)
	listed = models.BooleanField(default=True)

	def __str__(self) -> str:
		return self.name

class Campus(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(blank=True)
	address = models.CharField(max_length=255,blank=True)
	region = models.ForeignKey(
		Region,
		on_delete=models.CASCADE,
	)
	image = models.CharField(max_length=255, blank=True)
	map = models.CharField(max_length=255, blank=True)
	listed = models.BooleanField(default=True)

	def __str__(self) -> str:
		return self.name

class MenuCategory(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(blank=True)
	image = models.CharField(max_length=255, blank=True)
	campus = models.ForeignKey(
		Campus,
		on_delete=models.CASCADE,
	)
	listed = models.BooleanField(default=True)

	def __str__(self) -> str:
		return self.name

class MenuItem(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	category = models.ForeignKey(
		MenuCategory,
		on_delete=models.CASCADE,
	)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	listed = models.BooleanField(default=True)
	last_update = models.DateTimeField(auto_now=True)
	time_created = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	content  = models.TextField(blank=True)
	location = models.ForeignKey(
		Campus,
		on_delete=models.CASCADE,
	)
	image = models.CharField(max_length=255, blank=True)
	listed = models.BooleanField(default=True)
	event_start = models.DateTimeField()
	event_end = models.DateTimeField()
	last_update = models.DateTimeField(auto_now=True)
	time_created = models.DateTimeField(auto_now_add=True)

class User(models.Model):
	TYPE_STUDENT = 'S'
	TYPE_TEACHER = 'T'
	TYPE_CHOICES = [
		(TYPE_STUDENT, 'Student'),
		(TYPE_TEACHER, 'Teacher'),
	]
	type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=TYPE_STUDENT)
	campus = models.ForeignKey(
		Campus,
		on_delete=models.CASCADE,
	)
	name = models.CharField(max_length=255)
	number = models.CharField(max_length=255)