from django.urls import path
from restaurant.views import *

urlpatterns = [

    path("", home_view, name='home'),

]