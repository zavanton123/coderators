from django.urls import path

from snippet.views import HomeView, SnippetView, IndexView, AboutView, ClientView, ContactView

app_name = 'snippet'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('snippets/<int:pk>', SnippetView.as_view(), name='show_snippet_by_id'),
    path('index', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('client', ClientView.as_view(), name='client'),
    path('contact', ContactView.as_view(), name='contact'),
]
