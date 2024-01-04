from modeltranslation.translator import TranslationOptions, register
from restaurant.models import (AboutModel,Personal, Service,
                               Category, Menu, HomeHeader,
                               MainDetails, CateringMenu, CateringMenuCategories)

@register(AboutModel)
class AboutModelTranslationOptions(TranslationOptions):
    fields = ("head", "description")

@register(Personal)
class PersonalTranslationOptions(TranslationOptions):
    fields = ("position", )

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("name", "description")

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", )

@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ("food_name", "receipt")

@register(HomeHeader)
class HomeHeaderTranslationOptions(TranslationOptions):
    fields = ("main_text", "sub_text")

@register(MainDetails)
class MainDetailsTranslationOptions(TranslationOptions):
    fields = ("location", "working_time", "catering_menu_text", )

@register(CateringMenuCategories)
class CateringMenuCategoriesTranslationOptions(TranslationOptions):
    fields = ("name", )

@register(CateringMenu)
class CateringMenuTranslationOptions(TranslationOptions):
    fields = ("name", "ingredients")
