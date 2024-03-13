from rest_framework import serializers

from filestore.models import Folder


class FolderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Folder
        fields = ['id', 'name', 'parent_folder', 'user']
