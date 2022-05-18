from django.urls import path
from . import views

# URL Config
urlpatterns = [
	path('campus/', views.campus_list),
	path('campus/<int:id>', views.campus_detail),
	path('regions/', views.regions_list),
	path('regions/campuses/<int:id>', views.regions_campuses),
	path('menu/categories/', views.menu_category_list),
	path('menu/categories/<int:campus>', views.menu_category_campus),
	path('menu/items/', views.menu_items_list),
	path('menu/items/<int:category>', views.menu_items_category),
	path('events/', views.events_list),
	path('events/upcoming/', views.events_upcoming),
	path('users/', views.users_list),
]