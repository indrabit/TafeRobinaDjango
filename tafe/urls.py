from django.urls import path
from . import views

# URL Config
urlpatterns = [

	# Returns a list of all Regions.
	path('region/list', views.regions_list),

	# Returns Information on a given Campus.
	path('campus/<int:id>', views.campus_detail),

	# Returns a list of all Campuses.
	path('campus/list', views.campus_list),

	# Returns a list of all Campuses from a given Region.
	path('campus/list/<int:regionID>', views.region_campuses),
	
	# Returns the Trading Hours of a given Campus.
	path('campus/hours/<int:campusID>', views.campus_hours),

	# Returns a list of Resturants for a given Campus.
	path('resturant/list/<int:campusID>', views.resturant_list),

	# Returns the Trading Hours of a given Resturant.
	path('resturant/hours/<int:resturantID>', views.resturant_hours),

	# Returns a list of all Events.
	path('events/list', views.events_list),

	# Returns a list of all Upcoming Events.
	path('events/upcoming', views.events_upcoming),
]