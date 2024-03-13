# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from filestore.mixins.custome_mixins import FolderExistMixin
from filestore.models import File
from filestore.serilaizers.file_serializers import FileSerializer


class FileListCreateAPIView(
    FolderExistMixin,
    generics.ListCreateAPIView,
):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class FileRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
