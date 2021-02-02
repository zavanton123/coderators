from rest_framework import viewsets, permissions

from apps.snippet.api.api_snippet_serializers import CategorySerializer
from apps.snippet.models.category_models import Category


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
