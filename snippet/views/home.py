import logging

from django.views.generic import ListView

from snippet.models import Snippet

log = logging.getLogger(__name__)


class HomeView(ListView):
    template_name = 'snippet/home.html'
    context_object_name = 'snippets'
    ordering = ['-published_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Snippet.objects.filter(author=user)
        else:
            return Snippet.objects.all()


