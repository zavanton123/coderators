from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
    )
    slug = models.SlugField(
        max_length=100,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
