from django.urls import path

from apps.snippet.api.mock.mock_snippet_views import MockCategoriesApiView, MockCategoryApiView, MockTagsApiView, \
    MockTagApiView, \
    MockSnippetsApiView, MockSnippetApiView

name = 'mock_snippet'

urlpatterns = [
    path('categories/', MockCategoriesApiView.as_view(), name='mock-categories'),
    path('categories/<int:pk>/', MockCategoryApiView.as_view(), name='mock-category'),
    path('tags/', MockTagsApiView.as_view(), name='mock-tags'),
    path('tags/<int:pk>/', MockTagApiView.as_view(), name='mock-tag'),
    path('snippets/', MockSnippetsApiView.as_view(), name='mock-snippets'),
    path('snippets/<int:pk>/', MockSnippetApiView.as_view(), name='mock-snippet'),
]
