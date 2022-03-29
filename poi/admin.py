from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
	list_display = ['title', 'discription', 'image']
	list_per_page = 10