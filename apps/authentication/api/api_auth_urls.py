from django.urls import path, include

from apps.authentication.api.api_auth_views import demo

name = 'api_authentication'

urlpatterns = [
    path('', demo, name='demo'),

    # djoser authentication endpoints
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
