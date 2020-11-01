from django.contrib import admin

from snippet.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'latest_update']


admin.site.register(Snippet, SnippetAdmin)
