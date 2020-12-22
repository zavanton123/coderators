from django.contrib import admin

from snippet.models.category import Category
from snippet.models.snippet import Snippet
from snippet.models.tag import Tag


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'category', 'published_at', 'updated_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']


admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
