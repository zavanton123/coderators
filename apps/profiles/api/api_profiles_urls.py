from django.urls import path

from apps.profiles.api.api_profiles_views import ProfilesApiView, ProfileApiView

urlpatterns = [
    path('profiles/', ProfilesApiView.as_view()),
    path('profiles/<int:pk>/', ProfileApiView.as_view()),
]
