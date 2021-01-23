from django.urls import path

from apps.snippet.views.category_views import ShowCategories, UpdateCategory, DeleteCategory, ShowCategory, AddCategory

urlpatterns = [
    path('', ShowCategories.as_view(), name='show_categories'),
    path('<int:pk>', ShowCategory.as_view(), name='show_category'),
    path('add', AddCategory.as_view(), name='add_category'),
    path('update/<int:pk>', UpdateCategory.as_view(), name='update_category'),
    path('delete/<int:pk>', DeleteCategory.as_view(), name='delete_category'),
]
