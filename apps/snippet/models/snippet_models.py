from django.db import models
from django.urls import reverse

from apps.authentication.auth_models import CustomUser
from apps.snippet.models.category_models import Category
from apps.snippet.models.tag_models import Tag


class Snippet(models.Model):
    title = models.CharField(
        blank=False,
        max_length=1000
    )
    content = models.TextField(
        blank=False
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        related_name='snippets',
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        related_name='snippets',
        to=Tag,
        null=True,
        blank=True,
    )
    author = models.ForeignKey(
        to=CustomUser,
        null=True,
        on_delete=models.SET_NULL
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
        return reverse('snippet:show_snippet', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('snippet:delete_snippet', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return reverse('first-snippet:edit_snippet', kwargs={'pk': self.pk})
