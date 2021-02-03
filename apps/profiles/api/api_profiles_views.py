from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ProfilesApiView(APIView):
    def get(self, request, *args, **kwargs):
        profile = {
            'id': 1,
            'username': 'zavanton',
            'email': 'zavanton@yandex.ru',
            'first_name': 'Anton',
            'last_name': 'Zaviyalov',
            'is_staff': True,
            'date_joined': datetime.now(),
            'description': 'I am the admin',
            'experience': 'SENIOR',
            'avatar': 'http://some-image.jpg'
        }
        profile2 = profile
        data = [profile, profile2]
        return Response(data=data)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED)


class ProfileApiView(APIView):
    def get(self, request, *args, **kwargs):
        profile = {
            'id': 1,
            'username': 'zavanton',
            'email': 'zavanton@yandex.ru',
            'first_name': 'Anton',
            'last_name': 'Zaviyalov',
            'is_staff': True,
            'date_joined': datetime.now(),
            'description': 'I am the admin',
            'experience': 'SENIOR',
            'avatar': 'http://some-image.jpg'
        }
        return Response(data=profile)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)
