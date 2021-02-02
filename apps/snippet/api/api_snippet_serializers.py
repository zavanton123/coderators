import logging
from datetime import datetime

from django.template.defaultfilters import slugify
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.snippet.models import Snippet
from apps.snippet.models.category_models import Category
from apps.snippet.models.tag_models import Tag

log = logging.getLogger(__name__)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        name = validated_data.get('name', None)
        if name is not None:
            slug = slugify(name)
            instance.slug = slug
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        name = validated_data.get('name', None)
        if name is not None:
            slug = slugify(name)
            instance.slug = slug
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TagField(serializers.RelatedField):
    def get_queryset(self):
        return Tag.objects.all()

    def to_internal_value(self, data):
        tag = Tag(
            name=data,
            slug=slugify(data),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return tag

    def to_representation(self, value):
        return value.name


class SnippetSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    tags = TagField(
        many=True,
    )

    # todo zavanton - replace by hyperlink to user
    author = serializers.CharField(
        source='author.username',
        read_only=True,
    )

    class Meta:
        model = Snippet
        fields = [
            'id',
            'title',
            'content',
            'category',
            'tags',
            'author',
            'published_at',
            'updated_at',
        ]

    def create(self, validated_data):
        log.debug('zavanton - create')

        target_tags = []
        for tag in validated_data.pop('tags'):
            tags = Tag.objects.filter(name=tag.name)
            if tags.count() > 0:
                target_tag = tags.first()
            else:
                target_tag = Tag.objects.create(name=tag.name)
            target_tags.append(target_tag)

        request = self.context.get('request', None)
        if request is None:
            raise ValidationError('request must be provided to SnippetSerializer')

        # Snippet.objects.create(category=self._get_category(validated_data))

        return 'ok'

    def _get_category(self, validated_data):
        category_name = validated_data.pop('category')
        category_slug = slugify(category_name)
        categories = Category.objects.filter(slug=category_slug)
        if categories.count() > 0:
            return categories.first()
        else:
            return Category.objects.create(name=category_name)
