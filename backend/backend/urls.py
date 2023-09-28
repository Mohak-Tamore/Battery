from django.contrib import admin
from django.urls import path, include
from api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # station api url
    path('api/station',stationview),
    path('api/station/<int:pk>', stationdetailview),
    # users api url
    path('api/users',stationview),
    path('api/users/<int:pk>', stationdetailview)

]
