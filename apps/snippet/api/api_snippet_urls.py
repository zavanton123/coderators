from django.urls import path, include
from rest_framework import routers

from apps.snippet.api.api_snippet_views import CategoriesViewSet

name = 'api_snippet'

router = routers.DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]
