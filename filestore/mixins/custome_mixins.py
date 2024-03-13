from rest_framework.exceptions import ValidationError

from filestore.models import Folder


class UserOwnedMixin:
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FolderExistMixin:
    def perform_create(self, serializer):
        folder = Folder.objects.filter(user=self.request.user).first()
        if not folder:
            raise ValidationError("No folder found for the this user.")
        serializer.save(file_folder=folder)
