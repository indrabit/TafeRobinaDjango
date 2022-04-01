from django.contrib import admin
from django.utils.html import format_html
from . import models

# Register your models here.
@admin.register(models.Point)
class PointAdmin(admin.ModelAdmin):
	list_display = ['title', 'description', 'preview_image', 'generate_qr_code']
	list_per_page = 10

	def generate_qr_code(self, point):
		link = "https://quickchart.io/qr?size=500&text="+point.code
		return format_html('<a href="{}" target="_blank">Generate QR Code</a>', link)

	def preview_image(self, point):
		return format_html('<a href="{}" target="_blank">Preview Image</a>', point.image)