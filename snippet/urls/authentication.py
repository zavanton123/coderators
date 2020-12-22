from django.urls import path

from snippet.views import UserLoginView, UserLogoutView, RegisterView
from snippet.views.authentication import UserPasswordChangeView

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('password_change', UserPasswordChangeView.as_view(), name='password_change'),
    path('register', RegisterView.as_view(), name='register'),
]
