from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from snippet.views.home_views import HomeView
from snippet.views.misc_views import AboutView, ClientView, SendFeedback, ChooseLanguage

app_name = 'snippet'

urlpatterns = [
    # home view
    path('', HomeView.as_view(), name='home'),

    # snippets, categories, tags views
    path('snippets/', include('snippet.urls.snippet_urls')),
    path('categories/', include('snippet.urls.category_urls')),
    path('tags/', include('snippet.urls.tag_urls')),

    # authentication views
    # todo zavanton - is accounts necessary???
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include('snippet.urls.auth_urls')),

    # misc views
    path(_('about'), AboutView.as_view(), name='about'),
    path('clients', ClientView.as_view(), name='clients'),
    path('feedback', SendFeedback.as_view(), name='feedback'),
    path('language', ChooseLanguage.as_view(), name='language'),
]
