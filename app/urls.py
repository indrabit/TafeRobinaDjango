from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('points/', include('poi.urls')),
    # path('', include('campus.urls')),
    path('', include('tafe.urls')),
]