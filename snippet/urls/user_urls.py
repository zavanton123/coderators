from django.urls import path

from snippet.views import ViewUser
from snippet.views.user_views import UpdateUser, SetAvatar

urlpatterns = [
    path('', ViewUser.as_view(), name='view_user'),
    path('update/', UpdateUser.as_view(), name='update_user'),
    path('avatar', SetAvatar.as_view(), name='set_avatar'),
]
