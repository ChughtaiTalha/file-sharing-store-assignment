# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

from filestore.mixins.custome_mixins import UserOwnedMixin
from filestore.models import Folder
from filestore.serilaizers.folder_serializers import FolderSerializer


class FolderListCreateView(
    UserOwnedMixin,
    generics.ListCreateAPIView,
):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]


class FolderRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
