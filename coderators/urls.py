from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # simple captcha
    path('captcha/', include('captcha.urls')),
    path('', include('snippet.urls.main', namespace='first-snippet')),
]
