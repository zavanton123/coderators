from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('snippet:show_category', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('snippet:delete_category', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('snippet:update_category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
