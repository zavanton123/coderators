from django.template.defaultfilters import slugify
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.snippet.models import Snippet
from apps.snippet.models.category_models import Category
from apps.snippet.models.tag_models import Tag


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


class CategoryField(serializers.RelatedField):
    def get_queryset(self):
        return Category.objects.all()

    def to_internal_value(self, data):
        categories = Category.objects.filter(name=data)
        if categories.count() > 0:
            category = categories.first()
        else:
            category = Category.objects.create(name=data)
        return category

    def to_representation(self, value):
        return value.name


class TagField(serializers.RelatedField):
    def get_queryset(self):
        return Tag.objects.all()

    def to_internal_value(self, data):
        tags = Tag.objects.filter(name=data)
        if tags.count() > 0:
            tag = tags.first()
        else:
            tag = Tag.objects.create(name=data)
        return tag

    def to_representation(self, value):
        return value.name


class SnippetSerializer(serializers.ModelSerializer):
    category = CategoryField()

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
        request = self.context.get('request', None)
        if request is None:
            raise ValidationError('request must be provided to SnippetSerializer')

        user = request.user
        if not user.is_authenticated:
            raise ValidationError('user must be logged in to create new snippets')

        tags = validated_data.pop('tags')
        category = validated_data.pop('category')

        snippet = Snippet.objects.create(
            category=category,
            author=user,
            **validated_data
        )
        snippet.tags.set(tags)
        return snippet

    def update(self, instance, validated_data):
        request = self.context.get('request', None)
        if request is None:
            raise ValidationError('request must be provided to SnippetSerializer')

        user = request.user
        if not user.is_authenticated:
            raise ValidationError('user must be logged in to update new snippets')

        author = instance.author
        if author is None or user.pk != author.pk:
            raise ValidationError('snippet can be updated only by its author.')

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.tags.set(validated_data.pop('tags'))
        instance.save()
        return instance
