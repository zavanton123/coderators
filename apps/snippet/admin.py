from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.authentication.auth_models import CustomUser
from apps.snippet.models import Snippet
from apps.snippet.models.category_models import Category
from apps.snippet.models.tag_models import Tag


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (_('Custom fields'), {'fields': (
            'description',
            'experience',
            'avatar',
        )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Custom fields'), {'fields': (
            'description',
            'experience',
            'avatar',
        )}),
    )


class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'category', 'published_at', 'updated_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']


admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
