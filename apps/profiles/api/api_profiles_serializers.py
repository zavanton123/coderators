import logging

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentication.auth_models import CustomUser

log = logging.getLogger(__name__)


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_staff',
            'date_joined',
            'description',
            'experience',
            'avatar',
        ]
        read_only_fields = [
            'id',
            'date_joined',
        ]

    def create(self, validated_data):
        username = self.check_field('username', validated_data)
        email = self.check_field('email', validated_data)
        password = self.check_field('password', validated_data)
        first_name = validated_data.get('first_name', None)
        last_name = validated_data.get('last_name', None)
        is_staff = validated_data.get('is_staff', None)
        description = validated_data.get('description', None)
        experience = validated_data.get('experience', None)

        return CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            description=description,
            experience=experience
        )

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.username)
        instance.first_name = validated_data.get('first_name', instance.username)
        instance.last_name = validated_data.get('last_name', instance.username)
        instance.is_staff = validated_data.get('is_staff', instance.username)
        instance.experience = validated_data.get('experience', instance.username)
        instance.save()
        return instance

    def check_field(self, field_name, validated_data):
        field = validated_data.get(field_name, None)
        if field is None:
            raise ValidationError(field_name + ' is required for creating a new user')
        return field
