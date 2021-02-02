import debug_toolbar
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from coderators import settings

# yasg (swagger generator)
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# my api urls
api_urlpatterns = [
    # yasg (swagger and redoc urls)
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # my urls
    path('api/', include('apps.authentication.api.api_auth_urls')),
]

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # django rest framework login/logout
    path('api-auth', include('rest_framework.urls')),
    # simple captcha
    path('captcha/', include('captcha.urls')),
    # todo zavanton - examine the reason why an error is thrown when this url pattern is deleted
    # django-allauth
    path('accounts/', include('allauth.urls')),

    # my api urls
    path('', include(api_urlpatterns)),
]

# add i18n to urls
urlpatterns += i18n_patterns(
    # snippets app
    path('', include('apps.snippet.urls.main_urls', namespace='first-snippet')),
    path('auth/', include('apps.authentication.auth_urls', namespace='first-authentication')),
    path('profiles/', include('apps.profiles.profile_urls', namespace='first-profiles')),
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
