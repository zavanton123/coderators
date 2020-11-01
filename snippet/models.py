from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Snippet(models.Model):
    title = models.CharField(
        blank=False,
        max_length=1000
    )
    content = models.TextField(
        blank=False
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    latest_update = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snippet:show_snippet_by_id', kwargs={'pk': self.pk})
