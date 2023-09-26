from django.urls import path
from api import views


urlpatterns = [
    path('',views.home, name="home" ),
    # path('api/station',views.stationview, name="stationview" ),

]
