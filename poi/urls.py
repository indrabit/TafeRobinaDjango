from django.urls import path
from . import views

# URL Config
urlpatterns = [
	path('', views.points_list),
	path('<int:id>', views.point_detail)
]