from django.urls import path

from snippet.views import ShowSnippet, AddSnippet, UpdateSnippet, DeleteSnippet
from snippet.views.snippet import ShowSnippetsByCategory, ShowSnippetsByTag

snippets_urlpatterns = [
    path('<int:pk>', ShowSnippet.as_view(), name='show_snippet'),
    path('add', AddSnippet.as_view(), name='add_snippet'),
    path('edit/<int:pk>', UpdateSnippet.as_view(), name='edit_snippet'),
    path('delete/<int:pk>', DeleteSnippet.as_view(), name='delete_snippet'),
    path('category/<int:pk>', ShowSnippetsByCategory.as_view(), name='show_snippets_by_category'),
    path('tag/<int:pk>', ShowSnippetsByTag.as_view(), name='show_snippets_by_tag'),
]