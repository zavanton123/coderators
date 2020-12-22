from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, DeleteView

from snippet.forms.category import CreateCategoryForm
from snippet.models.category import Category


class ShowCategories(ListView):
    template_name = 'snippet/show_categories.html'
    context_object_name = 'categories'
    model = Category


class ShowCategory(DetailView):
    template_name = 'snippet/show_category.html'
    context_object_name = 'category'
    model = Category


class AddCategory(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'snippet/add_category.html'


class DeleteCategory(DeleteView):
    template_name = 'snippet/delete_category.html'
    success_url = reverse_lazy('snippet:show_categories')
    model = Category
