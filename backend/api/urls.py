from django.urls import path
from api import views


urlpatterns = [
    path('',views.home, name="home" ),
    # path('api/station',views.station, name="station" ),

]
