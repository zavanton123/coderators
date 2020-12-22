from django.urls import path

from snippet.views import ShowSnippet, AddSnippet, UpdateSnippet, DeleteSnippet
from snippet.views.authentication import LoginView, LogoutView, RegisterView, ProfileView
from snippet.views.category import ShowCategory, AddCategory, ShowCategories, DeleteCategory, UpdateCategory
from snippet.views.home import HomeView
from snippet.views.misc import AboutView, ClientView, ContactsView
from snippet.views.snippet import ShowSnippetsByCategory, ShowSnippetsByTag
from snippet.views.tag import AddTag, ShowTags, ShowTag, UpdateTag, DeleteTag

app_name = 'snippet'

urlpatterns = [
    # home view
    path('', HomeView.as_view(), name='home'),

    # snippet views
    path('snippets/<int:pk>', ShowSnippet.as_view(), name='show_snippet'),
    path('snippets/add', AddSnippet.as_view(), name='add_snippet'),
    path('snippets/edit/<int:pk>', UpdateSnippet.as_view(), name='edit_snippet'),
    path('snippets/delete/<int:pk>', DeleteSnippet.as_view(), name='delete_snippet'),
    path('snippets/category/<int:pk>', ShowSnippetsByCategory.as_view(), name='show_snippets_by_category'),
    path('snippets/tag/<int:pk>', ShowSnippetsByTag.as_view(), name='show_snippets_by_tag'),

    # category views
    path('categories/', ShowCategories.as_view(), name='show_categories'),
    path('categories/<int:pk>', ShowCategory.as_view(), name='show_category'),
    path('categories/add', AddCategory.as_view(), name='add_category'),
    path('categories/update/<int:pk>', UpdateCategory.as_view(), name='update_category'),
    path('categories/delete/<int:pk>', DeleteCategory.as_view(), name='delete_category'),

    # tag views
    path('tags/', ShowTags.as_view(), name='show_tags'),
    path('tags/add', AddTag.as_view(), name='add_tag'),
    path('tags/<int:pk>', ShowTag.as_view(), name='show_tag'),
    path('tags/update/<int:pk>', UpdateTag.as_view(), name='update_tag'),
    path('tags/delete/<int:pk>', DeleteTag.as_view(), name='delete_tag'),

    # authentication views
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),

    # misc views
    path('about', AboutView.as_view(), name='about'),
    path('clients', ClientView.as_view(), name='clients'),
    path('contacts', ContactsView.as_view(), name='contacts'),
]
