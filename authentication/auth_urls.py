from django.urls import path

from authentication.auth_views import UserPasswordChangeView, UserPasswordChangeDoneView, UserPasswordResetView, \
    UserPasswordResetConfirmView, UserPasswordResetDoneView, UserPasswordResetCompleteView, UserLoginView, \
    UserLogoutView, RegisterView

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('password_change', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register', RegisterView.as_view(), name='register'),
]
