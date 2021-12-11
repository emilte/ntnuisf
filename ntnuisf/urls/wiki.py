# imports
from django.urls import path

from ..views import wiki as wiki_views
# End: imports -----------------------------------------------------------------

app_name = 'wiki'

urlpatterns = [
    path('dashboard/', wiki_views.Dashboard.as_view(), name='dashboard'),
    path('folder/add/', wiki_views.AddFolder.as_view(), name='add_folder'),
    path('folder/edit/<int:model_id>/', wiki_views.EditFolder.as_view(), name='edit_folder'),
    path('page/add/', wiki_views.AddPage.as_view(), name='add_page'),
    path('page/edit/<int:model_id>/', wiki_views.EditPage.as_view(), name='edit_page'),
    path('page/<int:model_id>/', wiki_views.PageView.as_view(), name='page_view'),  # Order is important
]
