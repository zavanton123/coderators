from django.urls import path, include

from snippet.views import ShowSnippet, AddSnippet, UpdateSnippet, DeleteSnippet
from snippet.views.authentication import LoginView, LogoutView, RegisterView, ProfileView
from snippet.views.category import ShowCategory, AddCategory, ShowCategories, DeleteCategory, UpdateCategory
from snippet.views.home import HomeView
from snippet.views.misc import AboutView, ClientView, ContactsView
from snippet.views.snippet import ShowSnippetsByCategory, ShowSnippetsByTag
from snippet.views.tag import AddTag, ShowTags, ShowTag, UpdateTag, DeleteTag

app_name = 'snippet'

snippets_urlpatterns = [
    path('<int:pk>', ShowSnippet.as_view(), name='show_snippet'),
    path('add', AddSnippet.as_view(), name='add_snippet'),
    path('edit/<int:pk>', UpdateSnippet.as_view(), name='edit_snippet'),
    path('delete/<int:pk>', DeleteSnippet.as_view(), name='delete_snippet'),
    path('category/<int:pk>', ShowSnippetsByCategory.as_view(), name='show_snippets_by_category'),
    path('tag/<int:pk>', ShowSnippetsByTag.as_view(), name='show_snippets_by_tag'),
]

categories_urlpatterns = [
    path('', ShowCategories.as_view(), name='show_categories'),
    path('<int:pk>', ShowCategory.as_view(), name='show_category'),
    path('add', AddCategory.as_view(), name='add_category'),
    path('update/<int:pk>', UpdateCategory.as_view(), name='update_category'),
    path('delete/<int:pk>', DeleteCategory.as_view(), name='delete_category'),
]

tags_urlpatterns = [
    path('', ShowTags.as_view(), name='show_tags'),
    path('add', AddTag.as_view(), name='add_tag'),
    path('<int:pk>', ShowTag.as_view(), name='show_tag'),
    path('update/<int:pk>', UpdateTag.as_view(), name='update_tag'),
    path('delete/<int:pk>', DeleteTag.as_view(), name='delete_tag'),
]

urlpatterns = [
    # home view
    path('', HomeView.as_view(), name='home'),

    # snippets, categories, tags views
    path('snippets/', include(snippets_urlpatterns)),
    path('categories/', include(categories_urlpatterns)),
    path('tags/', include(tags_urlpatterns)),

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
