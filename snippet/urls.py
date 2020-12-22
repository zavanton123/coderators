from django.urls import path

from snippet.views import SnippetView, AddSnippet, UpdateSnippet, DeleteSnippet
from snippet.views.authentication import LoginView, LogoutView, RegisterView, ProfileView
from snippet.views.category import ShowCategory, AddCategory, ShowCategories, DeleteCategory, UpdateCategory
from snippet.views.home import HomeView
from snippet.views.misc import AboutView, ClientView, ContactsView

app_name = 'snippet'

urlpatterns = [
    # home view
    path('', HomeView.as_view(), name='home'),

    # snippet views
    path('snippets/<int:pk>', SnippetView.as_view(), name='show_snippet'),
    path('snippets/add', AddSnippet.as_view(), name='add_snippet'),
    path('snippets/edit/<int:pk>', UpdateSnippet.as_view(), name='edit_snippet'),
    path('snippets/delete/<int:pk>', DeleteSnippet.as_view(), name='delete_snippet'),

    # category views
    path('categories/', ShowCategories.as_view(), name='show_categories'),
    path('categories/<int:pk>', ShowCategory.as_view(), name='show_category'),
    path('categories/add', AddCategory.as_view(), name='add_category'),
    path('categories/update/<int:pk>', UpdateCategory.as_view(), name='update_category'),
    path('categories/delete/<int:pk>', DeleteCategory.as_view(), name='delete_category'),

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
