from django.urls import path

from apps.snippet.views.snippet_views import ShowSnippetsByCategory, ShowSnippetsByTag, ShowSnippet, AddSnippet, \
    UpdateSnippet, DeleteSnippet

urlpatterns = [
    path('<int:pk>', ShowSnippet.as_view(), name='show_snippet'),
    path('add', AddSnippet.as_view(), name='add_snippet'),
    path('edit/<int:pk>', UpdateSnippet.as_view(), name='edit_snippet'),
    path('delete/<int:pk>', DeleteSnippet.as_view(), name='delete_snippet'),
    path('category/<int:pk>', ShowSnippetsByCategory.as_view(), name='show_snippets_by_category'),
    path('tag/<int:pk>', ShowSnippetsByTag.as_view(), name='show_snippets_by_tag'),
]
