from rest_framework import serializers
from filestore.models import File


class FileSerializer(serializers.ModelSerializer):
    file_folder = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = File
        fields = '__all__'

