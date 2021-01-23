from django.urls import path, include
from django.utils.translation import gettext_lazy as _

from apps.snippet.views.home_views import HomeView
from apps.snippet.views.misc_views import AboutView, SendFeedback, ChooseLanguage

app_name = 'snippet'

urlpatterns = [
    # home view
    path('', HomeView.as_view(), name='home'),

    # snippets, categories, tags views
    path('snippets/', include('apps.snippet.urls.snippet_urls')),
    path('categories/', include('apps.snippet.urls.category_urls')),
    path('tags/', include('apps.snippet.urls.tag_urls')),

    # auth and user views
    path('auth/', include('apps.authentication.auth_urls')),
    path('profiles/', include('apps.profiles.profile_urls')),

    # misc views
    path(_('about'), AboutView.as_view(), name='about'),
    path('feedback', SendFeedback.as_view(), name='feedback'),
    path('language', ChooseLanguage.as_view(), name='language'),
]
