from django.contrib import admin
from restaurant.models import AboutModel, Personal, Service, Category, Menu, Contact

admin.site.register(AboutModel)
admin.site.register(Personal)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Contact)