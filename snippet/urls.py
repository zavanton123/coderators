from django.urls import path

from snippet.views import HomeView, SnippetView, IndexView, AboutView, ClientView, ContactsView, LoginView, \
    RegisterView, LogoutView, ProfileView, AddSnippet, DeleteSnippet, EditSnippet

app_name = 'snippet'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('snippets/<int:pk>', SnippetView.as_view(), name='show_snippet'),
    path('snippets/add', AddSnippet.as_view(), name='add_snippet'),
    path('snippets/delete/<int:pk>', DeleteSnippet.as_view(), name='delete_snippet'),
    path('snippets/edit/<int:pk>', EditSnippet.as_view(), name='edit_snippet'),
    path('index', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('clients', ClientView.as_view(), name='clients'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile')
]
