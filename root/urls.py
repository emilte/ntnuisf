# imports
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

import debug_toolbar
# End: imports -----------------------------------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
]

urlpatterns += static(prefix=settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
