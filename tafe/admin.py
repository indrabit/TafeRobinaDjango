from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'listed',
	]
	list_per_page = 10

@admin.register(models.Campus)
class CampusAdmin(admin.ModelAdmin):
	list_display = [
		'region',
		'name',
		'address',
		'phone',
		'listed',
	]
	list_per_page = 10

@admin.register(models.CampusHours)
class CampusHoursAdmin(admin.ModelAdmin):
	list_display = [
		'campus',
	]
	list_per_page = 10

@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
	list_display = [
		'campus',
		'name',
		'address',
		'phone',
		'listed',
	]
	list_per_page = 10

@admin.register(models.RestaurantHours)
class RestaurantHoursAdmin(admin.ModelAdmin):
	list_display = [
		'restaurant',
	]
	list_per_page = 10

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
	list_display = [
		'title',
		'location',
		'eventStart',
		'eventEnd',
		'listed',
	]
	list_per_page = 10

@admin.register(models.Industry)
class IndustryAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'listed',
	]
	list_per_page = 10

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
	list_display = [
		'type',
		'industry',
		'region',
		'campus',
	]
	list_per_page = 10