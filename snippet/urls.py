from django.urls import path

from snippet.views import HomeView

app_name = 'snippet'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
