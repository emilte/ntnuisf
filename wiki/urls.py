# imports
from django.urls import path
from django.views.i18n import JavaScriptCatalog
from django.views.generic.detail import DetailView

from wiki import views
from wiki import models as wiki_models
# End: imports -----------------------------------------------------------------

app_name = 'wiki'


urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),

    path('folder/add/', views.AddFolder.as_view(), name="add_folder"),
    path('folder/edit/<int:modelID>/', views.EditFolder.as_view(), name="edit_folder"),

    path('page/add/', views.AddPage.as_view(), name="add_page"),
    path('page/edit/<int:modelID>/', views.EditPage.as_view(), name="edit_page"),
    path('page/<int:modelID>/', views.PageView.as_view(), name="page_view"), # Order is important
]
