from django.urls import path
from . import views

# URL Config
urlpatterns = [
	path('campus/', views.campus_list),
	path('regions/', views.regions_list),
	path('menu/categories/', views.menu_category_list),
	path('menu/items/', views.menu_items_list),
	path('events/', views.events_list),
	path('events/upcoming/', views.events_upcoming),
	path('users/', views.users_list),
]