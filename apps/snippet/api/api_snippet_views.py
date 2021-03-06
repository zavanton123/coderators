from rest_framework import viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.snippet.api.api_snippet_serializers import CategorySerializer, TagSerializer, SnippetSerializer
from apps.snippet.models import Snippet
from apps.snippet.models.category_models import Category
from apps.snippet.models.tag_models import Tag


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SnippetsApiView(APIView):
    def get(self, request, *args, **kwargs):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(instance=snippets, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SnippetSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class SnippetApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(instance=snippet)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(data=request.data, instance=snippet, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(data=request.data, instance=snippet, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
