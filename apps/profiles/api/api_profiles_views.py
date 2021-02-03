import logging

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.auth_models import CustomUser
from apps.profiles.api.api_profiles_serializers import CustomUserSerializer

log = logging.getLogger(__name__)


class ProfilesApiView(APIView):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(instance=users, many=True, context={'request': request})
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ProfileApiView(APIView):
    def get(self, request, pk, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserSerializer(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk, *args, **kwargs):
        user = get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
