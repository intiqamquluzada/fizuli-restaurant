from django.urls import path
from restaurant.views import *

urlpatterns = [

    path("", home_view, name='home'),
    path("about/", about_view, name='about'),
    path("service/", service_view, name='service'),
    path("menu/", menu_view, name='menu'),

]