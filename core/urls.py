from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from restaurant.views import set_language
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('akm1n/', admin.site.urls),
    path("", include("restaurant.urls")),
    path('rosetta/', include('rosetta.urls')),
    path('set_language/<str:lang_code>/', set_language, name="set_lang"),
    path('i18n/', include('django.conf.urls.i18n')),

]

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [

    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
