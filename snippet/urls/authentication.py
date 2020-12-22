from django.urls import path

from snippet.views import MyLoginView, MyLogoutView, RegisterView

urlpatterns = [
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', MyLogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
]
