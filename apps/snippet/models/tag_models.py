from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
    )
    slug = AutoSlugField(
        populate_from=['name'],
        unique=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def get_absolute_url(self):
        return reverse('snippet:show_tag', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('snippet:update_tag', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('snippet:delete_tag', kwargs={'pk': self.pk})

    def get_snippets_url(self):
        return reverse('snippet:show_snippets_by_tag', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
