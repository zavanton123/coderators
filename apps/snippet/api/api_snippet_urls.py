from django.urls import path, include
from rest_framework import routers

from apps.snippet.api.api_snippet_views import CategoriesViewSet, TagsViewSet, SnippetsApiView

name = 'api_snippet'

router = routers.DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'tags', TagsViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', SnippetsApiView.as_view(), name='api-snippets'),
]
