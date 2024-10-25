from django.urls import path 
from .views import *

urlpatterns = [
    path("",MainPage.as_view(),name="MainPage"),
    path("menuitems",All_data,name="MenuItems"),
    
]
