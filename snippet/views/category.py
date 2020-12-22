from django.views.generic import DetailView

from snippet.models.category import Category


class ShowCategory(DetailView):
    template_name = 'snippet/show_category.html'
    context_object_name = 'category'
    model = Category
