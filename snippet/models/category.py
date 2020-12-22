from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        unique=True,
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
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
