from django.urls import path

from apps.profiles.profile_views import ViewProfile, UpdateProfile, SetAvatar

app_name = 'profiles'

urlpatterns = [
    path('', ViewProfile.as_view(), name='view_user'),
    path('update/', UpdateProfile.as_view(), name='update_user'),
    path('avatar', SetAvatar.as_view(), name='set_avatar'),
]