from django.contrib import admin

from snippet.models.category import Category
from snippet.models.snippet import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'category', 'published_at', 'updated_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']


admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Category, CategoryAdmin)
