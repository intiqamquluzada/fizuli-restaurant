from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from restaurant.models import (AboutModel, Personal, Service, Category, 
                               Menu, Contact, Reserve, HomeHeader, Subscribe, MainDetails, SocialMedia)

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ("name", "slug", "created_at")
    list_display_links = ("name", "slug")
    search_fields = ("name",)
    list_filter = ("created_at", "name")

    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("name", "slug")
    list_display_links = ("name", "slug")

    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(MainDetails)
class MainDetailsAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



@admin.register(HomeHeader)
class HomeHeaderAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(AboutModel)
class AboutAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Menu)
class MenuAdmin(TranslationAdmin):
    class Media:
        js = (

            'modeltranslation/js/tabbed_translation_fields.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        )

        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



admin.site.register(Personal)
admin.site.register(Contact)
admin.site.register(Reserve)
admin.site.register(Subscribe)
admin.site.register(SocialMedia)