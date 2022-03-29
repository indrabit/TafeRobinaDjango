from django.urls import path
from . import views

# URL Config
urlpatterns = [
	path('points/', views.points_list),
	path('points/<int:id>', views.point_detail)
]