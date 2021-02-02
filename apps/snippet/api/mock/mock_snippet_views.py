from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MockCategoriesApiView(APIView):
    def get(self, request, *args, **kwargs):
        cat1 = {
            'name': 'Some-category',
            'slug': 'some-slug',
            'created-at': 'some-time',
            'updated-at': 'some-time'
        }
        cat2 = {
            'name': 'Some-category',
            'slug': 'some-slug',
            'created-at': 'some-time',
            'updated-at': 'some-time'
        }
        data = [cat1, cat2]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED)


class MockCategoryApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Some-category',
            'slug': 'some-slug',
            'created-at': 'some-time',
            'updated-at': 'some-time'
        }
        return Response(data)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class MockTagsApiView(APIView):
    def get(self, request, *args, **kwargs):
        tag1 = {
            'name': 'Some-tag',
            'slug': 'some-slug',
            'created-at': 'some-time',
            'updated-at': 'some-time'
        }
        tag2 = {
            'name': 'Some-tag',
            'slug': 'some-slug',
            'created-at': 'some-time',
            'updated-at': 'some-time'
        }
        data = [tag1, tag2]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED)


class MockTagApiView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Some-tag',
            'slug': 'some-slug',
            'created-at': 'some-time',
            'updated-at': 'some-time'
        }
        return Response(data)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class MockSnippetsApiView(APIView):
    def get(self, request, *args, **kwargs):
        snippet1 = {
            'title': 'Some Title',
            'content': 'Some Content',
            'category': 'Some Category',
            'tags': [
                'Tag One',
                'Tag Two',
            ],
            'author': 'https://127.0.0.1:9999?api/users/123',
            'published_at': 'some-time',
            'updated_at': 'some-time'
        }
        snippet2 = snippet1
        data = [snippet1, snippet2]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED)


class MockSnippetApiView(APIView):
    def get(self, request, *args, **kwargs):
        snippet1 = {
            'title': 'Some Title',
            'content': 'Some Content',
            'category': 'Some Category',
            'tags': [
                'Tag One',
                'Tag Two',
            ],
            'author': 'https://127.0.0.1:9999?api/users/123',
            'published_at': 'some-time',
            'updated_at': 'some-time'
        }
        return Response(snippet1)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)
