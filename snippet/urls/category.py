from django.urls import path

from snippet.views import ShowCategory, AddCategory
from snippet.views.category import ShowCategories, UpdateCategory, DeleteCategory

categories_urlpatterns = [
    path('', ShowCategories.as_view(), name='show_categories'),
    path('<int:pk>', ShowCategory.as_view(), name='show_category'),
    path('add', AddCategory.as_view(), name='add_category'),
    path('update/<int:pk>', UpdateCategory.as_view(), name='update_category'),
    path('delete/<int:pk>', DeleteCategory.as_view(), name='delete_category'),
]