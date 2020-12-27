import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from coderators import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # simple captcha
    path('captcha/', include('captcha.urls')),
    path('', include('snippet.urls.main', namespace='first-snippet')),
]

if settings.DEBUG:
    urlpatterns += [
        # django debug toolbar
        path('__debug__/', include(debug_toolbar.urls))
    ]
