# -*- coding: utf-8 -*-
from django.urls import path

from .views.file_views import FileListCreateAPIView, FileRetrieveUpdateDestroyAPIView
from .views.folder_views import FolderRetrieveUpdateDestroyView, FolderListCreateView

urlpatterns = [
    path("folders/", FolderListCreateView.as_view(), name="folder-list-create"),
    path(
        "folders/<uuid:pk>/",
        FolderRetrieveUpdateDestroyView.as_view(),
        name="folder-retrieve-update-destroy",
    ),
    path("files/", FileListCreateAPIView.as_view(), name="file-list-create"),
    path(
        "files/<uuid:pk>/",
        FileRetrieveUpdateDestroyAPIView.as_view(),
        name="file-retrieve-update-destroy",
    ),
]
