from django.urls import path

from apps.authentication.auth_views import UserLoginView, UserLogoutView, UserPasswordChangeView, \
    UserPasswordChangeDoneView, UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView, \
    UserPasswordResetCompleteView, RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('password_change', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
