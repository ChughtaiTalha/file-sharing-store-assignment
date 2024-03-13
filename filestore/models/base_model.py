import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(editable=True, default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)