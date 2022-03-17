from . import views
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',views.home,name='home'),
    path('showdb',views.showdb,name='showdb'),
]