# imports
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.static import static

import debug_toolbar
# End: imports -----------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('ntnuisf.urls')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('accounts.urls')),
    path('allauth/', include('allauth.urls')),
    path('select2/', include('django_select2.urls')),
]

urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
