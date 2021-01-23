from django.urls import path

from authentication.views import ViewUser, UpdateUser, SetAvatar

urlpatterns = [
    path('', ViewUser.as_view(), name='view_user'),
    path('update/', UpdateUser.as_view(), name='update_user'),
    path('avatar', SetAvatar.as_view(), name='set_avatar'),
]