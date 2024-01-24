from django.urls import path
from project.views import *


urlpatterns = [
    path('', get_projects, name="get_projects"),
    path('project/<str:pk>/', get_projectsDetail, name="get_projectsDetail"),
    path('create-project/', create_project, name="create_project"),
    path('update-project/<str:pk>/', update_project, name="update_project"),
    path('delete-project/<str:pk>/', delete_project, name="delete_project"),
]
