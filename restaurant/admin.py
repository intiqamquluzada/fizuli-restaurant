from django.contrib import admin
from restaurant.models import (AboutModel, Personal, Service, Category, 
                               Menu, Contact, Reserve, HomeHeader, Subscribe, MainDetails, SocialMedia)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    list_display_links = ("name", "slug")
    search_fields = ("name",)
    list_filter = ("created_at", "name")


admin.site.register(AboutModel)
admin.site.register(Personal)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Contact)
admin.site.register(Reserve)
admin.site.register(HomeHeader)
admin.site.register(Subscribe)
admin.site.register(MainDetails)
admin.site.register(SocialMedia)