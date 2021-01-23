from django.urls import path

from profiles.profile_views import ViewProfile, UpdateProfile, SetAvatar

urlpatterns = [
    path('', ViewProfile.as_view(), name='view_user'),
    path('update/', UpdateProfile.as_view(), name='update_user'),
    path('avatar', SetAvatar.as_view(), name='set_avatar'),
]