from django.urls import path, include

from snippet.views import ProfileView
from snippet.views.home import HomeView
from snippet.views.misc import AboutView, ClientView, SendFeedback

app_name = 'snippet'

urlpatterns = [
    # home view
    path('', HomeView.as_view(), name='home'),

    # snippets, categories, tags views
    path('snippets/', include('snippet.urls.snippet')),
    path('categories/', include('snippet.urls.category')),
    path('tags/', include('snippet.urls.tag')),

    # authentication views
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('auth/', include('snippet.urls.authentication')),

    # misc views
    path('about', AboutView.as_view(), name='about'),
    path('clients', ClientView.as_view(), name='clients'),
    path('feedback', SendFeedback.as_view(), name='feedback'),
]
