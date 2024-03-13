# -*- coding: utf-8 -*-
from rest_framework import serializers

from filestore.models import Content


class ContentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Content
        fields = "__all__"
