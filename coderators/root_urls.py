import debug_toolbar
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from coderators import settings

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # simple captcha
    path('captcha/', include('captcha.urls')),
    # django-allauth
    path('accounts/', include('allauth.urls')),
]

# add i18n to urls
urlpatterns += i18n_patterns(
    # snippets app
    path('', include('apps.snippet.urls.main_urls', namespace='first-snippet')),
    prefix_default_language=False
)

# urls available only in DEBUG mode
if settings.DEBUG:
    # enable showing uploaded images
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [
        # django debug toolbar
        path('__debug__/', include(debug_toolbar.urls)),
    ]
