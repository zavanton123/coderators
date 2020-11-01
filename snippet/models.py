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
    published_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Published'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snippet:show_snippet_by_id', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('snippet:delete_snippet', kwargs={'pk': self.pk})
