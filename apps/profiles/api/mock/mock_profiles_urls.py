from django.urls import path

from apps.profiles.api.mock.mock_profiles_views import MockProfilesApiView, MockProfileApiView

urlpatterns = [
    path('profiles/', MockProfilesApiView.as_view()),
    path('profiles/<int:pk>/', MockProfileApiView.as_view()),
]
