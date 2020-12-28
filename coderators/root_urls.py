import debug_toolbar
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from coderators import settings

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # simple captcha
    path('captcha/', include('captcha.urls')),
]

# add i18n to urls
urlpatterns += i18n_patterns(
    # snippets app
    path('', include('snippet.urls.main_urls', namespace='first-snippet')),
    prefix_default_language=False
)

# urls available only in DEBUG mode
if settings.DEBUG:
    urlpatterns += [
        # django debug toolbar
        path('__debug__/', include(debug_toolbar.urls))
    ]
