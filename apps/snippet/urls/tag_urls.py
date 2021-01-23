from django.urls import path

from apps.snippet.views.tag_views import ShowTags, AddTag, ShowTag, UpdateTag, DeleteTag

urlpatterns = [
    path('', ShowTags.as_view(), name='show_tags'),
    path('add', AddTag.as_view(), name='add_tag'),
    path('<int:pk>', ShowTag.as_view(), name='show_tag'),
    path('update/<int:pk>', UpdateTag.as_view(), name='update_tag'),
    path('delete/<int:pk>', DeleteTag.as_view(), name='delete_tag'),
]