from django.contrib import admin
from django.utils.html import format_html
from . import models

# Register your models here.
@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'description',
		'preview_image',
	]
	list_per_page = 10

	def preview_image(self, location):
		return format_html('<img src="{}" width="250" height="150"/>', location.image)

@admin.register(models.Campus)
class CampusAdmin(admin.ModelAdmin):
	list_display = [
		'region',
		'name',
		'preview_image',
		'preview_map',
	]
	list_per_page = 10

	def preview_image(self, location):
		return format_html('<img src="{}" width="250" height="150"/>', location.image)

	def preview_map(self, location):
		return format_html('<a href="{}" target="_blank">Preview Map</a>', location.map)

@admin.register(models.MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
	list_display = [
		'campus',
		'name',
		'description',
		'preview_image',
	]
	list_per_page = 10

	def preview_image(self, menuCategory):
		return format_html('<img src="{}" width="250" height="150"/>', menuCategory.image)

@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
	list_display = [
		'category',
		'name',
		'price',
	]
	list_per_page = 10

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
	list_display = [
		'title',
		'description',
		'location',
		'event_start',
		'event_end',
		'preview_image',
	]
	list_per_page = 10

	def preview_image(self, event):
		return format_html('<img src="{}" width="250" height="150"/>', event.image)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
	list_display = [
		'type',
		'campus',
		'name',
		'number',
	]
	list_per_page = 10