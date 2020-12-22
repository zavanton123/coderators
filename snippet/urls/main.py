from django.urls import path, include

from snippet.urls.authentication import auth_urlpatterns
from snippet.urls.category import categories_urlpatterns
from snippet.urls.snippet import snippets_urlpatterns
from snippet.urls.tag import tags_urlpatterns
from snippet.views.home import HomeView
from snippet.views.misc import AboutView, ClientView, ContactsView

app_name = 'snippet'

urlpatterns = [
    # home view
    path('', HomeView.as_view(), name='home'),

    # snippets, categories, tags views
    path('snippets/', include(snippets_urlpatterns)),
    path('categories/', include(categories_urlpatterns)),
    path('tags/', include(tags_urlpatterns)),

    # authentication views
    path('auth/', include(auth_urlpatterns)),

    # misc views
    path('about', AboutView.as_view(), name='about'),
    path('clients', ClientView.as_view(), name='clients'),
    path('contacts', ContactsView.as_view(), name='contacts'),
]
