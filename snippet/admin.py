from django.contrib import admin

from snippet.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'published_at', 'updated_at']


admin.site.register(Snippet, SnippetAdmin)
